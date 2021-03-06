#!/usr/bin/python2
# -*- coding: utf8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab:fenc=utf-8
#
#    Copyright (C) 1999-2006  Keith Dart <keith@kdart.com>
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
This package implements the XHTML specification using the XML.POM (Pythonic
Object Model).

the XHTMLDocument class can be used to construct new XHTML documents.
There are many helper methods to construct a document from dtd objects.

You can use this as a pure-Python method of markup generation. No templates are required. It can be
used with the Pycopia web server framework, or other frameworks such as Django.

The general pattern of constructor methods is this. If a method starts with *get_* then it is a
factory method that construct an elemement node that is not attached to the document tree. Methods
starting with *add_* call the same factory method but also adds (appends) the new object to the
document tree at the node where it was called. Methods starting with *new_* add new element to the
document tree that may be a more complex operation, or take additional parameters or build more
complex subtrees. They also return the new object.

When complete, the tree can be serialized by stringifying it, or by using the `emit` method.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import itertools

try:
    from PIL import Image
except ImportError:
    Image = None

from pycopia.urlparse import quote_plus
from pycopia.textutils import identifier
from pycopia.aid import partial, Enums, Enum

from pycopia import dtds
from pycopia.XML import POM, XMLVisitorContinue, ValidationError, XMLPathError

get_class = dtds.get_class

NBSP = POM.ASIS(b"&#160;")
TRUE = True
FALSE = False

MIME_XHTML = b"application/xhtml+xml"
MIME_HTML = b"text/html"

# tags defined to be inline - use for BeautifulWriter and other type checks
INLINE_SPECIAL = ["span", "bdo", "object", "img", "map"]
# (br is ommitted on purpose - looks better)
INLINE_FONTSTYLE = [ "tt", "i", "b", "big", "small"]
INLINE_PHRASE = [ "em", "strong", "dfn", "code", "samp", "kbd",
    "cite", "var", "abbr", "acronym", "q", "sub", "sup"]
INLINE_FORM = ["input", "select", "textarea", "label", "button"]
INLINE = ["a"] + INLINE_SPECIAL + INLINE_FONTSTYLE + INLINE_PHRASE + INLINE_FORM


# make strings into Text objects, otherwise verify Element object.
def check_object(obj):
    if obj is None:
        return NBSP
    if type(obj) in (str, unicode, int, float, long):
        return POM.Text(str(obj))
    if isinstance(obj, POM.ElementNode):
        return obj
    raise ValidationError("bad initializer object: should be string or ElementNode instance.")

def create_POM(data, dtd):
    """Given a python object, produce reasonable markup from that. Return
    a valid POM node.

    Dictionaries produce sections (divs) where key names are the class
    attribute name; lists produce ordered lists; Sets produce unordered
    lists; Tuples produce a fragment collection (invisible), an
    ElementNode is taken as-is, and strings return as Text nodes.
    Callables are called with the DTD, and the return value checked.
    """
    if data is None:
        return NBSP # Good representation of nothing?
    it = type(data)
    if it is dict:
        creator = FlowCreator(dtd)
        outer = POM.Fragments()
        for name, content in data.iteritems():
            div = creator.get_section(name)
            div.append(create_POM(content, dtd))
            outer.append(div)
        return outer
    elif it is list:
        creator = FlowCreator(dtd)
        ol = creator.get_ordered_list()
        for item in data:
            ol.add_item(item)
        return ol
    elif it is set:
        creator = FlowCreator(dtd)
        ul = creator.get_unordered_list()
        for item in data:
            ul.add_item(item)
        return ul
    elif it is tuple:
        frags = POM.Fragments()
        for item in data:
            frags.append(create_POM(item, dtd))
        return frags
    elif it is unicode:
        return POM.Text(data)
    elif isinstance(data, POM.ElementNode):
        return data
    elif it is FunctionType:
        return check_object(data(dtd))
    else:
        return POM.Text(data)

# Pre-compute type here for speed.
FunctionType = type(create_POM)

# counters to ensure unique IDs in a document.
class _Counter(object):
    def __init__(self, name):
        self.name = name
        self.val = 0
    def __iter__(self):
        return self
    def next(self):
        self.val += 1
        return val
    def reset(self):
        self.val = 0
    def __str__(self):
        return b"%s%s" % (self.name, self.val)
    __call__ = __str__


class XHTMLComment(POM.Comment):
    pass

class FlowMixin(object):
    def _init(self, dtd):
        self.dtd = dtd

    def add2class(self, name):
        add2class(self, name)

    def get_javascript(self, text=None, src=None):
        sc = self.dtd.Script(type="text/javascript")
        if text:
            sc.add_cdata(text)
            return sc
        elif src:
            sc.src = src
        return sc

    def add_javascript(self, text=None, src=None):
        sc = self.get_javascript(text, src)
        self.append(sc)
        return sc

    def get_dtd_element(self, name):
        try:
            return getattr(self.dtd, identifier(name))
        except AttributeError:
            raise ValidationError("No element: %s" % (name,))

    def make_node(self, name, attribs, *content):
        if name in ("Text", "ASIS", "Fragments"):
            elemclass = getattr(POM, name)
        elif name == "_":
            return NBSP
        elif name == "JS": # special javascript handler
            Scr = self.get_dtd_element("Script")
            elem = Scr(type="text/javascript")
            for cont in content:
                elem.add_cdata(cont)
            return elem
        elif name == "code": # special dynamic node handler
            if attribs:
                return DynamicNode(content[0], **attribs)
            else:
                return DynamicNode(content[0])
        else:
            elemclass = self.get_dtd_element(name)

        if attribs:
            elem = elemclass(**attribs)
        else:
            elem = elemclass()

        for cont in content:
            if isinstance(cont, (POM.ElementNode, POM.Text, POM.ASIS)):
                elem.append(cont)
            else:
                elem.add_text(cont)
        return elem

    def get_nodemaker(self):
        def _make_node(container, name, attribs, *contents):
            return container.make_node(name, attribs, *contents)
        return partial(_make_node, self)
    nodemaker = property(get_nodemaker)

    def create_markup(self, data):
        """Create markup (a POM object tree) from Python objects."""
        return create_POM(data, self.dtd)

    def get_creator(self):
        def _creator(container, data):
            return create_POM(data, container.dtd)
        return partial(_creator, self)
    creator = property(get_creator)

    def add_element(self, name, **kwargs):
        obj = get_container(self.dtd, name, kwargs)
        self.append(obj)
        return obj

    # generic element factory
    def get_new_element(self, name, **kwargs):
        return get_container(self.dtd, name, kwargs)
    get = get_new_element

    def new_image(self, _imagefile, _alt=None, **kwargs):
        check_flag(kwargs, "ismap")
        if Image is not None:
            try:
                im = Image.open(_imagefile)
            except IOError:
                pass
            else:
                x, y = im.size
                kwargs["width"] = str(x)
                kwargs["height"] = str(y)
                try:
                    im.close()
                except:
                    pass
                del im
        kwargs["src"] = _imagefile # XXX adjust for server alias?
        if _alt:
            kwargs["alt"] = _alt
        img = self.dtd.Img(**kwargs)
        self.append(img)
        return img

    def get_image(self, **kwargs):
        check_flag(kwargs, "ismap")
        img =  self.dtd.Img(**kwargs)
        return img

    def add_image(self, **kwargs):
        img = self.get_image(**kwargs)
        self.append(img)
        return img

    def get_object(self, _params=None, **kwargs):
        check_flag(kwargs, "declare")
        Object = get_class(self.dtd, "Object", (ObjectMixin, self.dtd.Object))
        obj = Object(**kwargs)
        obj._init(self.dtd)
        if _params:
            if isinstance(_params, dict):
                for name, value in _params.items():
                    obj.add_param(name, value)
            elif isinstance(_params, (list, tuple)):
                for name, value in _params: # list of tuples
                    obj.add_param(name, value)
        return obj

    def add_object(self, _params=None, **kwargs):
        obj = self.get_object(_params, **kwargs)
        self.append(obj)
        return obj

    # Some MochiKit integration.
    def connect(self, signame, dest, func=None):
        """http://mochikit.com/doc/html/MochiKit/Signal.html#fn-connect"""
        self.add_javascript('connect("%s", "%s", %s);' % (self.id, signame, dest))

    def disconnect(self, *signals):
        if signals:
            self.add_javascript('disconnectAll("%s", %s);' % (
                 self.id,
                 ", ".join(map(repr, signals))))
        else:
            self.add_javascript('disconnectAll("%s");' % (self.id, ))


class ObjectMixin(FlowMixin):
    def add_param(self, name, value=None, valuetype="data", type=None, id=None):
        assert valuetype in ("data", "ref", "object")
        p = self.dtd.Param(name=name, valuetype=valuetype)
        if value:
            p.set_attribute("value", value)
        if type:
            p.set_attribute("type", type)
        if id:
            p.set_attribute("id", id)
        self.insert(0, p) # param elements should precede all other content.


# null formatter for primary table column construction.
def _NULLRenderer(nodemaker, obj):
    return obj

# container for other objects (Div) for layout purposes
# Use CSS to define the area properties.
class ContainerMixin(FlowMixin):

    def get_section(self, _name, **kwargs):
        Section = get_class(self.dtd, "Section%s" % _name, (ContainerMixin, self.dtd.Div))
        kwargs["class_"] = _name
        sect = Section(**kwargs)
        sect._init(self.dtd)
        return sect

    def add_section(self, _name, **kwargs):
        sect = self.get_section(_name, **kwargs)
        self.append(sect)
        return sect

    def new_section(self, _name, _data, **kwargs):
        sect = self.get_section(_name, **kwargs)
        _data = create_POM(_data, self.dtd)
        sect.append(_data)
        self.append(sect)
        return sect

    def get_inline(self, _name, **kwargs):
        Inline = get_class(self.dtd, "Inline%s" % _name, (InlineMixin, self.dtd.Span))
        kwargs["class_"] = str(_name)
        sect = Inline(**kwargs)
        sect._init(self.dtd)
        return sect

    def add_inline(self, _name, **kwargs):
        sect = self.get_inline(_name, **kwargs)
        self.append(sect)
        return sect

    def new_inline(self, _name, _obj, **kwargs):
        il = self.get_inline(_name, **kwargs)
        _obj = create_POM(_obj, self.dtd)
        il.append(_obj)
        self.append(il)
        return il

    def get_break(self, **kwargs):
        return self.dtd.Br(**kwargs)

    def add_break(self, **kwargs):
        br = self.dtd.Br(**kwargs)
        self.append(br)
        return br

    def get_para(self, **attribs):
        Para = get_class(self.dtd, "Para", (InlineMixin, FormMixin, self.dtd.P))
        p = Para(**attribs)
        p._init(self.dtd)
        return p

    def add_para(self, **attribs):
        p = self.get_para(**attribs)
        self.append(p)
        return p

    def new_para(self, data, **attribs):
        p = self.get_para(**attribs)
        t = create_POM(data, self.dtd)
        p.append(t)
        self.append(p)
        return p

    def get_header(self, level, text, **kwargs):
        hobj = get_inlinecontainer(self.dtd, "H%d" % (level,), kwargs)
        hobj.append(POM.Text(text))
        return hobj

    def add_header(self, level, text, **kwargs):
        hobj = self.get_header(level, text, **kwargs)
        self.append(hobj)
        return hobj

    def get_ruler(self, **kwargs):
        return self.dtd.Hr(**kwargs)

    def add_ruler(self, **kwargs):
        hr = self.dtd.Hr(**kwargs)
        self.append(hr)
        return hr

    def get_unordered_list(self, **attribs):
        Unordered = get_class(self.dtd, "Unordered", (ListMixin, self.dtd.Ul))
        ul = Unordered(**attribs)
        ul._init(self.dtd)
        return ul

    def get_ordered_list(self, **attribs):
        Ordered = get_class(self.dtd, "Ordered", (ListMixin, self.dtd.Ol))
        ol = Ordered(**attribs)
        ol._init(self.dtd)
        return ol

    def add_unordered_list(self, items, **kwargs):
        ul = self.get_unordered_list(**kwargs)
        for item in items:
            li = ul.add(self.dtd.Li)
            li.append(check_object(item))
        self.append(ul)
        return ul

    def add_ordered_list(self, items, **kwargs):
        ol = self.get_ordered_list(**kwargs)
        for item in items:
            li = ol.add(self.dtd.Li)
            li.append(check_object(item))
        self.append(ol)
        return ol

    def get_definition_list(self, **attribs):
        DL = get_class(self.dtd, "DefinitionList", (DefinitionListMixin, self.dtd.Dl))
        dl = DL(**attribs)
        dl._init(self.dtd)
        return dl

    def add_definition_list(self, **attribs):
        dl = self.get_definition_list(**attribs)
        self.append(dl)
        return dl

    def get_anchor(self, **attribs):
        return self.dtd.A(**attribs)

    def add_anchor(self, **attribs):
        a = self.dtd.A(**attribs)
        self.append(a)
        return a

    def new_anchor(self, obj, **attribs):
        a = self.dtd.A(**attribs)
        a.append(check_object(obj))
        self.append(a)
        return a

    def add_comment(self, text):
        comment = XHTMLComment(text)
        self.append(comment)

    def get_table(self, **kwargs):
        XHTMLTable = get_class(self.dtd, "XHTMLTable", (TableMixin, self.dtd.Table))
        t= XHTMLTable(**kwargs)
        t._init(self.dtd)
        return t

    def add_table(self, **kwargs):
        t  = self.get_table(**kwargs)
        self.append(t)
        return t

    def new_table(self, rowiter, coliter, headings=(), renderer=_NULLRenderer,
                               **kwargs):
        """Construct a new table. Row iterator adds rows with first column
        filled in with object, formatted by calling the renderer callback
        with the object (which should return something). Column iterator
        fills in extra columns by using a callback with a nodemaker and
        row object as parameters. Supply a tuple of values for the
        "headings" parameter to set the table headings.
        Other keyword arguments are passed on as table attributes.
        """
        tbl = self.add_table(**kwargs)
        tbl_id = kwargs.get("id")
        NM = self.get_nodemaker()
        cycler = itertools.cycle(["row1", "row2"]) # For alternating row styles.
        # headings
        if headings:
            tbl.new_headings(*headings)
        # table body
        if tbl_id: # if table has id, then cells get an id.
            for y, obj in enumerate(rowiter):
                row = tbl.new_row()
                setattr(row, "class_", cycler.next())
                col = row.add_column(id="%s_%s_%s" % (tbl_id, y, 0))
                col.append(check_object(renderer(NM, obj)))
                for x, callback in enumerate(coliter):
                    col = row.add_column(id="%s_%s_%s" % (tbl_id, y, x+1))
                    col.append(check_object(callback(NM, obj)))
        else:
            for obj in rowiter:
                row = tbl.new_row()
                setattr(row, "class_", cycler.next())
                col = row.add_column()
                col.append(check_object(renderer(NM, obj)))
                for callback in coliter:
                    col = row.add_column()
                    col.append(check_object(callback(NM, obj)))
        return tbl

    def new_table_from_GenericTable(self, table, renderer=_NULLRenderer, **kwargs):
        """Construct an XHTML table from a pycopia.table.GenericTable object.
        """
        tbl = self.add_table(**kwargs)
        NM = self.get_nodemaker()
        cycler = itertools.cycle(["row1", "row2"]) # For alternating row styles.
        # headings
        if table.headings:
            tbl.new_headings(*table.headings)
        if table.title:
            tbl.caption(table.title)
        for table_row in table:
            row = tbl.new_row()
            setattr(row, "class_", cycler.next())
            for cell in table_row:
                col = row.add_column()
                col.append(check_object(renderer(NM, cell)))
        return tbl

    def get_form(self, **kwargs):
        XHTMLForm = get_class(self.dtd, "XHTMLForm", (FormMixin, self.dtd.Form))
        f = XHTMLForm(**kwargs)
        f._init(self.dtd)
        method = kwargs.get("method")
        if method is None:
            f.method = method = "post"
        action = kwargs.get("action")
        if action is None:
            f.action = "."
        enctype = kwargs.get("enctype")
        if enctype is None:
            if method == "get":
                f.enctype="application/x-www-form-urlencoded"
            elif method == "post":
                f.enctype="multipart/form-data"
            else:
                raise ValidationError("invalid form method: %r" % (method,))
        return f

    def add_form(self, **kwargs):
        f = self.get_form(**kwargs)
        self.append(f)
        return f

    def get_preformat(self, **kwargs):
        Preform = get_class(self.dtd, "Preform", (InlineMixin, self.dtd.Pre))
        pre = Preform(**kwargs)
        pre._init(self.dtd)
        return pre

    def add_preformat(self, **kwargs):
        p = self.get_preformat(**kwargs)
        self.append(p)
        return p

    def new_preformat(self, text, **kwargs):
        p = self.get_preformat(**kwargs)
        t = POM.Text(text)
        p.append(t)
        self.append(p)
        return p


def get_container(dtd, name, kwargs):
    name = identifier(name)
    base = getattr(dtd, name)
    if base.CONTENTMODEL.is_empty():
        return base(**kwargs)
    if issubclass(base, ContainerMixin):
        return base(**kwargs)
    cls = get_class(dtd, name, (ContainerMixin, base))
    obj = cls(**kwargs)
    obj._init(dtd)
    return obj

def get_inlinecontainer(dtd, name, kwargs):
    name = identifier(name)
    base = getattr(dtd, name)
    cls = get_class(dtd, name, (InlineMixin, base))
    obj = cls(**kwargs)
    obj._init(dtd)
    return obj

class XHTMLDocument(POM.POMDocument, ContainerMixin):
    """XHTMLDocument is a complete XHTML document.
    """
    MIMETYPE="application/xhtml+xml"

    def initialize(self):
        root = self.dtd._Root()
        self.set_root(root)
        head = get_container(self.dtd, "Head", {})
        body = get_container(self.dtd, "Body", {})
        root.append(head)
        root.append(body)
        # Set convenient direct accessors to main HTML document parts.
        root.head = head
        root.body = body

    # default body shortcuts are properties.
    head = property(lambda self: self.get_path("/html/head"))
    body = property(lambda self: self.get_path("/html/body"))

    # Produce sequence of IDs with base name and sequence number postfix.
    def next_id(self, name):
        try:
            self._COUNTERS[name].next()
            return str(self._COUNTERS[name])
        except KeyError:
            ctr = self._COUNTERS[name] = _Counter(name)
            return str(ctr)

    # helpers for adding specific elements
    def add_title(self, title):
        ti = self.head.add(self.dtd.Title)
        ti.append(POM.Text(title))

    def _get_title(self):
        try:
            return self.get_path("/html/head/title")
        except XMLPathError:
            return None
    title = property(_get_title, add_title)

    def add_stylesheet(self, url):
        self.head.add(self.dtd.Link, rel="stylesheet",
                                        type="text/css", href=url)
    def _get_stylesheet(self):
        try:
            return self.head.get_element('link[@rel="stylesheet"]')
        except XMLPathError:
            return None

    def _del_stylesheet(self):
        ss = self.head.get_element('link[@rel="stylesheet"]')
        if ss:
            ss.destroy()
    stylesheet = property(_get_stylesheet, add_stylesheet)

    def add_stylesheets(self, namelist):
        for url in namelist:
            if "/" not in url:
                url = "/media/css/" + url
            self.add_stylesheet(url)

    stylesheets = property(None, add_stylesheets)

    # embedded stylesheet
    def _set_style(self, text):
        try:
            st = self.head.get_element("style")
        except XMLPathError:
            st = self.head.add(self.dtd.Style, type="text/css")
        st.add_cdata(text)

    def _get_style(self):
        try:
            return self.head.get_element("style")
        except XMLPathError:
            return None

    def _del_style(self):
        try:
            st = self.head.get_element("style")
        except XMLPathError:
            pass
        else:
            st.destroy()

    style = property(_get_style, _set_style, _del_style)

    def add_javascript2head(self, text=None, url=None):
        if text:
            sc = self.head.add(self.dtd.Script, type=b"text/javascript")
            sc.add_cdata(text)
        elif url:
            sc = self.head.add(self.dtd.Script,
                           type=b"text/javascript", src=url)

    def _add_js_list(self, jslist):
        for url in jslist:
            if "/" not in url:
                url = "/media/js/" + url
            self.head.add(self.dtd.Script, type=b"text/javascript", src=url)

    scripts = property(None, _add_js_list, None, "Add a list of javascript file names.")

    def _get_javascript(self):
        try:
            return self.head.get_element("script")
        except XMLPathError:
            return None

    def _del_javascript(self):
        sc = self.head.get_element("script")
        if sc:
            sc.destroy()

    javascript = property(_get_javascript, add_javascript2head, _del_javascript)
    javascriptlink = property(_get_javascript,
                    lambda self, v: self.add_javascript2head(url=v))


    # general add methods
    def append(self, obj, **kwargs):
        if type(obj) is str:
            obj = get_container(self.dtd, obj, **kwargs)
        self.body.append(obj)

    def insert(self, ind, obj, **kwargs):
        if type(obj) is str:
            obj = get_container(self.dtd, obj, **kwargs)
        self.body.insert(ind, obj)


# container for inline markup
class InlineMixin(FlowMixin):

    def get_inline(self, _name, **kwargs):
        Inline = get_class(self.dtd, "Inline%s" % (_name,), (InlineMixin, self.dtd.Span))
        kwargs["class_"] = str(_name)
        span = Inline(**kwargs)
        span._init(self.dtd)
        return span

    def add_inline(self, _name, **kwargs):
        span = self.get_inline(_name, **kwargs)
        self.append(span)
        return span

    def new_inline(self, _name, _obj, **attribs):
        _obj = create_POM(_obj, self.dtd)
        try:
            ilmc = getattr(self.dtd, _name)
        except AttributeError:
            raise ValidationError("%s: not valid for this DTD." % (_name,))
        Inline = get_class(self.dtd, "Inline%s" % (_name,), (InlineMixin, ilmc))
        il = Inline(**attribs)
        il._init(self.dtd)
        if _obj:
            il.append(_obj)
        self.append(il)
        return il

    def text(self, text):
        return self.add_text(" "+str(text))

    def nbsp(self):
        self.append(NBSP)

    def span(self, obj, **attribs):
        return self.new_inline("Span", obj, **attribs)

    def anchor(self, obj, **attribs):
        return self.new_inline("A", obj, **attribs)

    def bold(self, obj, **attribs):
        return self.new_inline("B", obj, **attribs)

    def italic(self, obj, **attribs):
        return self.new_inline("I", obj, **attribs)

    def teletype(self, obj, **attribs):
        return self.new_inline("Tt", obj, **attribs)

    def big(self, obj, **attribs):
        return self.new_inline("Big", obj, **attribs)

    def small(self, obj, **attribs):
        return self.new_inline("Small", obj, **attribs)

    def em(self, obj, **attribs):
        return self.new_inline("Em", obj, **attribs)

    def strong(self, obj, **attribs):
        return self.new_inline("Strong", obj, **attribs)

    def dfn(self, obj, **attribs):
        return self.new_inline("Dfn", obj, **attribs)

    def code(self, obj, **attribs):
        return self.new_inline("Code", obj, **attribs)

    def quote(self, obj, **attribs):
        return self.new_inline("Q", obj, **attribs)
    Q = quote

    def sub(self, obj, **attribs):
        return self.new_inline("Sub", obj, **attribs)

    def sup(self, obj, **attribs):
        return self.new_inline("Sup", obj, **attribs)

    def samp(self, obj, **attribs):
        return self.new_inline("Samp", obj, **attribs)

    def kbd(self, obj, **attribs):
        return self.new_inline("Kbd", obj, **attribs)

    def var(self, obj, **attribs):
        return self.new_inline("Var", obj, **attribs)

    def cite(self, obj, **attribs):
        return self.new_inline("Cite", obj, **attribs)

    def abbr(self, obj, **attribs):
        return self.new_inline("Abbr", obj, **attribs)

    def acronym(self, obj, **attribs):
        return self.new_inline("Acronym", obj, **attribs)


class ListMixin(ContainerMixin):
    def add_item(self, obj, **attribs):
        obj = create_POM(obj, self.dtd)
        Item = get_class(self.dtd, "Item", (InlineMixin, self.dtd.Li))
        li = Item(**attribs)
        li._init(self.dtd)
        li.append(obj)
        self.append(li)
        return li


# Special support methods for XHTML tables. The makes it easy to produce simple
# tables.
class TableMixin(ContainerMixin):
    # set document dtd so methods can access it to create sub-elements
    def _init(self, dtd):
        self.dtd = dtd
        self._t_caption = None # only one
        self._headings = self.dtd.Tr()
        self._footer = self.dtd.Tr()
        self._t_rows = []

    def caption(self, content, **kwargs):
        # enforce the rule that there is only one caption, and it is first
        # element in the table.
        cap = self.dtd.Caption(**kwargs)
        cap.append(check_object(content))
        self._t_caption = cap

    @property
    def headings(self):
        return self._headings # a row (tr) object.

    @property
    def footer(self):
        return self._footer # a row (tr) object.

    def set_heading(self, col, val, **kwargs):
        """Set heading at column <col> (origin 1) to <val>."""
        val = check_object(val)
        # auto-fill intermediate cells, if necessary.
        for inter in range(col - len(self._headings)):
            self._headings.append(self.dtd.Th(**kwargs))
        th = self._headings[col-1]
        th.append(val)
        return th

    def new_headings(self, *args, **kwargs):
        self._headings = self.dtd.Tr(**kwargs)
        for hv in args:
            th = self.dtd.Th()
            self._headings.append(th)
            th.append(check_object(hv))
        return self._headings

    def new_footer(self, *args, **kwargs):
        self._footer = self.dtd.Tr(**kwargs)
        for hv in args:
            th = self.dtd.Th()
            self._footer.append(th)
            th.append(check_object(hv))
        return self._footer

    def get_row(self, **kwargs):
        Row = get_class(self.dtd, "Row", (RowMixin, self.dtd.Tr))
        row = Row(**kwargs)
        row._init(self.dtd)
        return row

    def add_row(self, **kwargs):
        row = self.get_row(**kwargs)
        self._t_rows.append(row)
        return row

    def new_row(self, *args, **kwargs):
        row = self.get_row(**kwargs)
        for obj in args:
            if type(obj) is list:
                for nobj in obj:
                    t = create_POM(obj, self.dtd)
                    td = self.dtd.Td()
                    td.append(t)
                    row.append(td)
            else:
                t = create_POM(obj, self.dtd)
                td = self.dtd.Td()
                td.append(t)
                row.append(td)
        self._t_rows.append(row)
        return row

    def set_cell(self, col, row, val):
        val = check_object(val)
        for inter in range(row - len(self._t_rows)):
            newrow = self.dtd.Tr()
            self._t_rows.append(newrow)
            for inter in range(col):
                newrow.append(self.dtd.Td())

        r = self._t_rows[row-1]
        while 1:
            try:
                td = r[col-1]
            except IndexError:
                r.append(self.dtd.Td())
            else:
                break
        td.append(val)
        return td

    def get_cell(self, col, row):
        r = self._t_rows[row-1]
        return r[col-1]

    def delete(self, col, row):
        r = self._t_rows[row-1]
        del r[col-1]
        if len(r) == 0:
            del self._t_rows[row-1]

    def __str__(self):
        return self.encode(self.encoding or POM.DEFAULT_ENCODING)

    def encode(self, encoding):
        self._verify_attributes()
        name = self._name.encode(encoding)
        s = []
        s.append(b"<%s%s>" % (name, self._attr_str(encoding)))
        if self._t_caption:
            s.append(self._t_caption.encode(encoding))
        thead = self.dtd.Thead()
        thead.append(self._headings)
        s.append(thead.encode(encoding))
        tbody = self.dtd.Tbody()
        for row in self._t_rows:
            tbody.append(row)
        s.append(tbody.encode(encoding))
        tfoot = self.dtd.Tfoot()
        tfoot.append(self._footer)
        s.append(tfoot.encode(encoding))
        s.append((b"</%s>" % name))
        return b"".join(s)

    def emit(self, fo, encoding=None):
        encoding = encoding or self.encoding
        fo.write(self.encode(encoding))


class RowMixin(ContainerMixin):
    def get_column(self, **kwargs):
        TD = get_class(self.dtd, "Column", (ContainerMixin, self.dtd.Td))
        col = TD(**kwargs)
        col._init(self.dtd)
        return col

    def add_column(self, **kwargs):
        col = self.get_column(**kwargs)
        self.append(col)
        return col

    def new_column(self, *args, **kwargs):
        col = self.get_column(**kwargs)
        for obj in args:
            stuff = create_POM(obj, self.dtd)
            col.append(stuff)
        self.append(col)
        return col


class FormMixin(ContainerMixin):

    def fetch_form_values(self, container=None):
        rv = container or []
        visitor = partial(self._get_node_value, rv)
        for node in self._children:
            node.walk(visitor)
        return rv

    def _get_node_value(self, container, node):
        if isinstance(node, self.dtd.Input):
            if node.disabled:
                return
            if node.type == "checkbox" and node.checked:
                container.append((node.name, node.value))
            elif node.type == "radio" and node.checked:
                container.append((node.name, node.value))
            elif node.type == "text" and node.value:
                container.append((node.name, node.value))
            elif node.type == "password" and node.value:
                container.append((node.name, node.value))
            elif node.type == "submit" and node.value:
                container.append((node.name, node.value))
            elif node.type == "hidden" and node.value:
                container.append((node.name, node.value))
        elif isinstance(node, self.dtd.Select):
            if node.disabled:
                return
            for opt in node.getall(self.dtd.Option):
                if opt.selected and not opt.disabled:
                    container.append((node.name, opt.value))
            raise XMLVisitorContinue
        elif isinstance(node, self.dtd.Textarea):
            if not node.disabled:
                text = node.get_text()
                if text:
                    container.append((node.name, text))
            raise XMLVisitorContinue

    def fetch_form_elements(self):
        """Return active form element nodes, grouped by name in a dictionary."""
        rv = {}
        visitor = partial(self._check_node, rv)
        for node in self._children:
            node.walk(visitor)
        return rv

    def _check_node(self, container, node):
        if isinstance(node, (self.dtd.Input, self.dtd.Select, self.dtd.Textarea)):
            try:
                l = container[node.name]
            except KeyError:
                l = container[node.name] = []
            l.append(node)
            raise XMLVisitorContinue

    def get_textarea(self, name, text=None, rows=4, cols=60, **kwargs):
        check_flag(kwargs, "readonly")
        check_flag(kwargs, "disabled")
        textclass = get_class(self.dtd, "TextWidget", (TextareaMixin, self.dtd.Textarea))
        ta = textclass(name=name, rows=rows, cols=cols, **kwargs)
        ta._init(self.dtd)
        if text:
            ta.append(check_object(text))
        return ta

    def add_textarea(self, name, text=None, rows=4, cols=60, **kwargs):
        ta = self.get_textarea(name, text, rows, cols, **kwargs)
        self.append(ta)
        return ta

    def get_input(self, **kwargs):
        check_flag(kwargs, "readonly")
        check_flag(kwargs, "checked")
        check_flag(kwargs, "disabled")
        check_flag(kwargs, "autofocus")
        inputclass = get_class(self.dtd, "InputWidget", (InputMixin, self.dtd.Input))
        inp = inputclass(**kwargs)
        inp._init(self.dtd)
        return inp

    def add_input(self, **kwargs):
        inp = self.get_input(**kwargs)
        self.append(inp)
        return inp

    def get_fieldset(self, legend=None, **kwargs):
        FieldSet = get_class(self.dtd, "FieldSet", (FormMixin, self.dtd.Fieldset))
        fs = FieldSet(**kwargs)
        fs._init(self.dtd)
        if legend:
            lg = self.dtd.Legend()
            lg.append(check_object(legend))
            fs.append(lg)
        return fs

    def add_fieldset(self, legend=None, **kwargs):
        fs = self.get_fieldset(legend, **kwargs)
        self.append(fs)
        return fs

    def get_textinput(self, name, label=None, default="", maxlength=255, **kwargs):
        if label:
            lbl = self.get_label(label, "id_%s" % (name,))
        else:
            lbl = None
        inp = self.dtd.Input(type="text", name=name, value=default,
                maxlength=maxlength, id="id_%s" % (name,), **kwargs)
        return lbl, inp

    def add_textinput(self, name, label=None, default="", maxlength=255, **kwargs):
        lbl, inp = self.get_textinput(name, label, default, maxlength, **kwargs)
        if lbl:
            self.append(lbl)
        self.append(inp)
        return inp

    def get_password(self, name, label=None, default="", maxlength=255):
        if label:
            lbl = self.get_label(label, "id_%s" % (name,))
        else:
            lbl = None
        inp = self.dtd.Input(type="password", name=name, value=default,
                maxlength=maxlength, id="id_%s" % (name,))
        return lbl, inp

    def add_password(self, name, label=None, default="", maxlength=255):
        lbl, inp = self.get_password(name, label, default, maxlength)
        if lbl:
            self.append(lbl)
        self.append(inp)
        return inp

    def get_label(self, text, _for=None):
        lbl = self.dtd.Label()
        if _for:
            lbl.set_attribute("for_", _for) # 'for' is a keyword...
        lbl.append(check_object(text))
        return lbl

    def add_label(self, text, _for=None):
        lbl = self.get_label(text, _for)
        self.append(lbl)
        return lbl

    def get_select(self, enums, **kwargs):
        check_flag(kwargs, "multiple")
        check_flag(kwargs, "disabled")
        sl = self.dtd.Select(**kwargs)
        self._add_options(sl, enums)
        return sl

    def _add_options(self, sl, enums):
        et =  type(enums)
        if et is Enums and enums:
            for i, name in enums.choices:
                opt = self.dtd.Option(value=i)
                opt.append(POM.Text(name))
                sl.append(opt)
            return
        if et is dict and enums:
            for key, val in enums.items():
                opt = self.dtd.Optgroup(label=key)
                self._add_options(opt, val)
                sl.append(opt)
            return
        if et is tuple and enums:
            name, value = enums
            opt = self.dtd.Option(value=value)
            opt.append(POM.Text(name))
            return
        if et is list and enums:
            for item in enums:
                it = type(item)
                if it is tuple: # add "selected" item by adding (value, flag)
                    opt = self.dtd.Option(value=item[0])
                    opt.append(POM.Text(item[1]))
                    if len(item) > 2 and item[2]:
                        opt.selected = "selected"
                elif it is dict: # make option groups by passing dictionaries
                    for key, val in item.items():
                        optgrp = self.dtd.Optgroup(label=key)
                        sl.append(optgrp)
                        self._add_options(optgrp, val)
                elif it is Enum: # a named number
                    opt = self.dtd.Option(value=int(item))
                    opt.append(POM.Text(item))
                elif it is list: # nested lists will be flattened
                    self._add_options(sl, item)
                else:
                    opt = self.dtd.Option(value=item)
                    opt.append(POM.Text(item))
                sl.append(opt)
            return
        else:
            opt = self.dtd.Option(value=enums)
            opt.append(POM.Text(enums))
            sl.append(opt)
            return

    def add_select(self, enums, **kwargs):
        sl = self.get_select(enums, **kwargs)
        self.append(sl)
        return sl

    def get_radiobuttons(self, name, choices, vertical=False, checked=0, **kwargs):
        fs = self.get_fieldset(name, **kwargs)
        for value, valname in choices:
            ID = "id_%s%s" % (name, value)
            l = self.get_label(valname, ID)
            inp = self.dtd.Input(type="radio", name=name, value=value, id=ID)
            if value == checked:
                inp.checked = "checked"
            fs.append(l)
            fs.append(inp)
            if vertical:
                fs.append(self.dtd.Br())
        return fs

    def add_radiobuttons(self, name, choices, vertical=False, checked=0, **kwargs):
        fs = self.add_fieldset(name, **kwargs)
        for value, valname in choices:
            ID = "id_%s%s" % (name, value)
            fs.add_label(valname, ID)
            inp = self.dtd.Input(type="radio", name=name, value=value, id=ID)
            if value == checked:
                inp.checked = "checked"
            fs.append(inp)
            if vertical:
                fs.append(self.dtd.Br())
        return fs

    def get_checkboxes(self, name, choices, vertical=False, **kwargs):
        fs = self.get_fieldset(name, **kwargs)
        for value, valname in choices:
            ID = "id_%s%s" % (name, value)
            l = self.get_label(valname, ID)
            fs.append(l)
            fs.append(self.dtd.Input(type="checkbox", name=name, value=value, id=ID))
            if vertical:
                fs.append(self.dtd.Br())
        return fs

    def add_checkboxes(self, name, choices, vertical=False, **kwargs):
        fs = self.add_fieldset(name, **kwargs)
        for value, valname in choices:
            ID = "id_%s%s" % (name, value)
            fs.add_label(valname, ID)
            fs.append(self.dtd.Input(type="checkbox", name=name, value=value, id=ID))
            if vertical:
                fs.append(self.dtd.Br())
        return fs

    def add_fileinput(self, name="fileinput", default=None):
        inp = self.dtd.Input(type="file", name=name, value=default)
        self.append(inp)
        return inp

    def add_hidden(self, name, value):
        inp = self.dtd.Input(type="hidden", name=name, value=value)
        self.append(inp)
        return inp

    # the following methods mimic the cliutils functions
    def choose(self, somelist, defidx=0, prompt="choose"):
        ID = "id_%s" % id(somelist)
        self.add_label(prompt, ID)
        # make the defidx "selected"
        orig = somelist.pop(defidx)
        somelist.insert(defidx, (orig, True))
        return self.add_select(somelist, id=ID)

    def yes_no(self, prompt, name="yes_no", default=True):
        fs = self.add_fieldset(prompt)
        fs.set_attribute("class_", "yes_no")
        for i, item in enumerate(["Yes", "No"]):
            inp = self.dtd.Input(type="radio", name=name, value=i)
            if i == 0 and default:
                inp.checked = "checked"
            if i == 1 and not default:
                inp.checked = "checked"
            fs.append(inp)
            fs.append(check_object(item))
        return fs


class WidgetBase(InlineMixin):
    pass


class StringWidget(WidgetBase):
    pass

class PasswordWidget(StringWidget):
    pass

class TextareaMixin(WidgetBase):
    def set_disabled(self, val=True):
        if val:
            self.disabled = "disabled"
        else:
            del self.disabled

    def set_readonly(self, val=True):
        if val:
            self.readonly = "readonly"
        else:
            del self.readonly


class InputMixin(WidgetBase):
    """type = (text | password | checkbox | radio | submit | reset |
    file | hidden | image | button) """
    def set_checked(self, val=True):
        if val:
            self.checked = "checked"
        else:
            del self.checked

    def set_disabled(self, val=True):
        if val:
            self.disabled = "disabled"
        else:
            del self.disabled

    def set_readonly(self, val=True):
        if val:
            self.readonly = "readonly"
        else:
            del self.readonly

    def set_autofocus(self, val=True):
        if val:
            self.autofocus = "autofocus"
        else:
            del self.autofocus


class DefinitionListMixin(object):
    def _init(self, dtd):
        self.dtd = dtd

    def add_definition(self, term, data, **kwargs):
        dt = self.dtd.Dt(**kwargs)
        dt.append(check_object(term))
        dd = self.dtd.Dd(**kwargs)
        dd.append(create_POM(data, self.dtd))
        self.append(dt)
        self.append(dd)

    def add_definitions(self, defmap, **kwargs):
        """Add a set of definitions from a dictionary, where the keys are
        the terms and the values are the data.
        """
        items = defmap.items()
        items.sort()
        for term, data in items:
            self.add_definition(term, data)


class FlowCreator(FormMixin, InlineMixin, DefinitionListMixin):
    def __init__(self, dtd):
        self.dtd = dtd


class DynamicNode(object):
    """A psuedo-node that emits markup that is dynamic. This really wraps
    a markup generator as a node object, so that it may be emitted later
    with dynamic data.
    """

    def __init__(self, _method, *args, **kwargs):
        self._method = _method
        self._args = args
        self._kwargs = kwargs
        self._parent = None
        self.encoding = POM.DEFAULT_ENCODING

    def __str__(self):
        return self.encode(self.encoding)

    def encode(self, encoding):
        return self._method(*self._args, **self._kwargs).encode(encoding)

    def emit(self, fo, encoding):
        fo.write(self._method(*self._args, **self._kwargs).encode(encoding))

    def __repr__(self):
        cl = self.__class__
        return "%s.%s(%r)" % (cl.__module__, cl.__name__, self._method)

    # dummy methods, to satisfy ElementNode interface.
#    def get_escape_length(self):
#        return len(self.data)
    def insert(self, data, encoding=None):
        raise NotImplementedError("Cannot insert into DynamicNode")
    def destroy(self):
        self._parent = None
    def detach(self):
        self._parent = None
    def _fullpath(self):
        if self._parent:
            return "%s = %r" % (self._parent._fullpath(), repr(self._method))
        else:
            return repr(self._method)
    fullpath = property(_fullpath)
    def walk(self, visitor):
        visitor(self)
    def matchpath(self, pe):
        return 0
    def has_children(self):
        return 0
    def has_attributes(self):
        return 0


def check_flag(kwargs, name):
    """enforce XML rules for flags."""
    flag = kwargs.get(name)
    if flag is not None:
        if flag:
            kwargs[name] = name
        else:
            del kwargs[name]

def add2class(node, name):
    """Maintains space-separated class names."""
    attr = node.get_attribute("class")
    if attr is None:
        node.set_attribute("class", name)
    else:
        attr += " "
        attr += name
        node.set_attribute("class", attr)

def get_url(params, base=None):
    """Return a URL properly encoded for inclusion as an href. Provide a
    dictionary of parameters and an optional base path."""
    enc = '&amp;'.join(['%s=%s' % (quote_plus(k), quote_plus(v)) for k,v in params.items()])
    if base:
        return base + "?" + enc
    else:
        return enc

class URL(dict):
    def __init__(self, base):
        self._base = base
        super(URL, self).__init__()
    def __str__(self):
        return get_url(self, self._base)



class GenericDocument(POM.POMDocument, FlowMixin):
    """Generic markup document to be used as a default.
    """
    MIMETYPE="text/xml"


# danger: hard-coded config. ;-)
# This maps a doctype, generically determined by the root element name, to
# a specific document class and default doctype. It simultaneously
# contains the mimtype to document class mapping.
# TODO doctype registry.
_DOCMAP = {
    "html": (XHTMLDocument, dtds.XHTML),
    MIME_XHTML: (XHTMLDocument, dtds.XHTML),
    MIME_HTML: (XHTMLDocument, dtds.XHTML),
}

def get_document_class(doctype=None, mimetype=None):
    if doctype:
        dtobject = dtds.get_doctype(doctype)
        if dtobject:
            return _DOCMAP.get(dtobject.name.lower(), (GenericDocument, doctype))
        else:
            return (GenericDocument, None) # no doctype defined
    elif mimetype:
        return _DOCMAP.get(mimetype, (GenericDocument, dtds.XHTML1_TRANSITIONAL))
    else:
        raise ValueError("You must supply a doctype or a mimetime")


# Document constructors. Use one of these to get your XHTML document.

# Primary document factory for new XHTML class of documents.
def new_document(doctype=dtds.XHTML11, mimetype=None, encoding=POM.DEFAULT_ENCODING, lang=None):
    doc = xhtml_factory(doctype=doctype, mimetype=mimetype, encoding=encoding, lang=lang)
    doc.initialize()
    return doc


# Document factory for new sparse documents. Used by parser.
def xhtml_factory(doctype=None, mimetype=None, encoding=POM.DEFAULT_ENCODING, lang=None):
    docclass, defdt = get_document_class(doctype=doctype, mimetype=mimetype)
    if doctype is None:
        doctype = defdt
    doc = docclass(doctype=doctype, lang=lang, encoding=encoding)
    return doc

