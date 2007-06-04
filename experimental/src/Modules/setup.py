#!/usr/bin/python2.4
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
# 
# $Id$
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
Extra compiled modules for pyNMS are installed here.

"""

from distutils.core import Extension, setup

readline = Extension('readline', ['readline.c'],
                    define_macros=[("HAVE_RL_COMPLETION_MATCHES", None)],
                    library_dirs=['/usr/lib/termcap'],
                   libraries=["readline", "ncurses"])

mmap = Extension('mmap', ['mmapmodule.c'],)
fcntl = Extension('fcntl', ['fcntlmodule.c'],)

setup(name="patches", ext_modules=[readline, fcntl, mmap])

