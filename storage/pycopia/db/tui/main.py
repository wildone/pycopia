#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
#    Copyright (C) 2010 Keith Dart <keith@dartworks.biz>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

__doc__ = """
Storage editor. Edit data in the Pycopia database. Start with a list of
editable tables. Select and move to locations to create, update, and delete
entries.

Keys:
    Generally, use arrow keys to navigate and press Enter to select items.

    ESC : Quit the program
    Tab : Move focus to different button or area. Arrow keys also work.
    F1  : This Help
    F2  : Reset the application to initial condition.

Shortcuts for creating test cases:
    F5  : Create a new test case in the database.
    F6  : Create a new test suite in the database.

Shortcuts for creating equipment and environments.
    F9  : Create a new equipment entry.
    F10 : Create a new environment entry.

"""

import sys
import urwid

from pycopia.db import models
from pycopia.db.tui import widgets


class DBEditor(object):

    def __init__(self, session):
        self.loop =None
        self.session = session
        header = urwid.AttrMap(urwid.Text("Storage Editor", align="center"), "head")
        self.footer = urwid.AttrMap(
                urwid.Text([
                        ("key", "ESC"), " Quit  ",
                        ("key", "Tab"), " Move Selection  ",
                        ("key", "F1"), " Help  ",
                        ("key", "F2"), " Reset ",
                        ("key", "F5"), " Add Test Case ",
                        ("key", "F6"), " Add Test Suite ",
                        ("key", "F9"), " Add Equipment ",
                        ("key", "F10"), " Add Environment ",
                    ]),
                "foot")
        self.reset()
        self.top = urwid.Frame(urwid.AttrMap(self.form, 'body'), header=header, footer=self.footer)

    def run(self):
        self.loop = urwid.MainLoop(self.top, widgets.PALETTE,
                unhandled_input=self.unhandled_input, pop_ups=True,
                event_loop=urwid.GLibEventLoop())
        self.loop.run()
        self.loop = None

    def unhandled_input(self, k):
        if k == "esc":
            self._popform(None)
        elif k == "f1":
            self.show_help()
        elif k == "f2":
            self.reset()
            self.top.body = self.form
        elif k == "f5":
            self.create_form(models.TestCase)
        elif k == "f16":
            self.create_form(models.TestSuite)
        elif k == "f9":
            self.create_form(models.Equipment)
        elif k == "f10":
            self.create_form(models.Environment)

    def reset(self):
        self._formtrail = []
        self.form = widgets.TableForm(self.session)
        urwid.connect_signal(self.form, 'pushform', self._pushform)

    def _restore_footer(self, loop, user_data):
        self.top.set_footer(self.footer)

    def _pushform(self, form, newform):
        self._formtrail.append((form.__class__, form.session, form.modelclass, form.row))
        urwid.disconnect_signal(form, 'pushform', self._pushform)
        urwid.connect_signal(newform, 'pushform', self._pushform)
        urwid.connect_signal(newform, 'popform', self._popform)
        self.form = newform
        self.top.body = self.form

    def _popform(self, form):
        if self._formtrail:
            formclass, sess, modelclass, row = self._formtrail.pop()
            self.form = formclass(sess, modelclass, row)
            urwid.connect_signal(self.form, 'pushform', self._pushform)
            self.top.body = self.form
        else:
            raise urwid.ExitMainLoop()

    def message(self, msg):
        self.top.set_footer(urwid.AttrWrap(urwid.Text(msg), "foot"))
        self.loop.set_alarm_in(5.0, self._restore_footer)

    def list_form(self, modelclass):
        form = widgets.get_list_form(self.session, modelclass)
        urwid.emit_signal(self.form, 'pushform', self.form, form)

    def create_form(self, modelclass):
        form = widgets.get_create_form(self.session, modelclass)
        urwid.emit_signal(self.form, 'pushform', self.form, form)

    def edit_form(self, row):
        form = widgets.get_edit_form(self.session, row)
        urwid.emit_signal(self.form, 'pushform', self.form, form)

    def show_help(self):
        hd = HelpDialog()
        urwid.connect_signal(hd, 'close', lambda hd: self._restoreform())
        self.top.body = hd

    def _restoreform(self):
        self.top.body = self.form



class HelpDialog(urwid.WidgetWrap):
    signals = ['close']

    def __init__(self):
        close_button = urwid.Button(("selectable", "OK"))
        urwid.connect_signal(close_button, 'click', lambda button:self._emit("close"))
        lb =urwid.LineBox(urwid.Filler(urwid.Pile([urwid.Text(__doc__), close_button]), valign="top"))
        self.__super.__init__(lb)


def main(argv):
    sess = models.get_session()
    try:
        app = DBEditor(sess)
        app.run()
    finally:
        sess.close()


if __name__ == "__main__":
    import sys
    from pycopia import debugger
    try:
        main(sys.argv)
    except:
        ex, val, tb = sys.exc_info()
        from pycopia import IOurxvt
        io = IOurxvt.UrxvtIO()
        debugger.post_mortem(tb, ex, val, io)
        io.close()
