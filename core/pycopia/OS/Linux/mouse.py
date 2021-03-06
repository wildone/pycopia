#!/usr/bin/python2
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
# 
#    Copyright (C) 2011  Keith Dart <keith@kdart.com>
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

"""

"""

from pycopia.OS.Linux import Input
from pycopia.OS.Linux import event




class Mouse(Input.EventDevice):
    DEVNAME = 'Mouse'

    def initialize(self):
        self._motion_cb = lambda ev: None
        self._button_cb = lambda ev: None
        self._wheel_cb = lambda ev: None

    def register_motion(self, cb):
        self._motion_cb = cb

    def register_button(self, cb):
        self._button_cb = cb

    def register_wheel(self, cb):
        self._wheel_cb = cb

    def poll(self):
        while 1:
            ev = self.read()
            if ev.evtype == event.EV_REL:
                if ev.code == event.REL_WHEEL:
                    self._wheel_cb(ev)
                else:
                    self._motion_cb(ev)
            elif ev.evtype == event.EV_KEY:
                self._button_cb(ev)

    read_handler = poll


class MotionEventHandler(object):
    def __init__(self):
        self._disp = {
            event.REL_X: self._relx,
            event.REL_Y: self._rely,
            event.REL_Z: self._relz,
        }

    def __call__(self, ev):
        self._disp[ev.code](ev.value)

    def _relx(self, value):
        return self.movement(value, 0, 0)

    def _rely(self, value):
        return self.movement(0, value, 0)

    def _relz(self, value):
        return self.movement(0, 0, value)

    def movement(self, x, y, z):
        pass


class ButtonEventHandler(object):

    def __init__(self):
        self._disp = {
            event.BTN_LEFT: self.left_button,
            event.BTN_RIGHT: self.right_button,
            event.BTN_MIDDLE: self.middle_button,
        }

    def __call__(self, ev):
        self._disp[ev.code](ev.value)

    def left_button(self, value):
        pass

    def middle_button(self, value):
        pass

    def right_button(self, value):
        pass

class WheelEventHandler(object):

    def __call__(self, ev):
        if ev.value == -1:
            return self.down()
        elif ev.value == 1:
            return self.up()

    def up(self):
        pass

    def down(self):
        pass


if __name__ == "__main__":
    mouse = Mouse()
    mouse.find()
    print mouse
    print "devname:", mouse.name
    print "driverversion: 0x%x" % (mouse.get_driverversion(),)
    print "deviceid:", mouse.get_deviceid()
    print "features:", mouse.get_features()

    def print_ev(event):
        print event

    class MotionPrint(MotionEventHandler):
        def movement(self, x, y, z):
            print "X:", x, "Y:", y, "Z:", z

    class ButtonPrint(ButtonEventHandler):
        def left_button(self, value):
            print "Left button: ", value

        def middle_button(self, value):
            print "Middle button: ", value

        def right_button(self, value):
            print "Right button: ", value

    class WheelPrint(WheelEventHandler):
        def up(self):
            print "Wheel UP"

        def down(self):
            print "Wheel DOWN"

    mouse.register_motion(MotionPrint())
    mouse.register_button(ButtonPrint())
    mouse.register_wheel(WheelPrint())

    try:
        while 1:
            mouse.poll()
    except KeyboardInterrupt:
        pass
    mouse.close()

