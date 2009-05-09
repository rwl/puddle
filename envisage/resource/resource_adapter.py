#------------------------------------------------------------------------------
# Copyright (C) 2007 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" An editor with content provided by a workspace resource.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import pickle as pickle

from os.path import getmtime

from enthought.io.api import File

from enthought.traits.api import \
    Property, Bool, Adapter, adapts, Instance, Float, HasTraits

from enthought.traits.ui.api import View, Item, Group

from enthought.pyface.workbench.api import TraitsUIEditor

from i_resource import IResource

#------------------------------------------------------------------------------
#  "PickleFileIResourceAdapter" class:
#------------------------------------------------------------------------------

class PickleFileIResourceAdapter(Adapter):
    """ Adapts a "File" with pickled content to 'IResource'.
    """
    # Declare the interfaces this adapter implements for its client:
    adapts(File, to=IResource, when="adaptee.ext=='.pkl'")

    # The object that is being adapted.
    adaptee = Instance(File)

    # Is the object 'dirty'?
#    dirty = Bool(False)

    # The time of the last modification
#    m_time = Float

    def save(self, obj):
        """ Save to file """

        fd = None
        try:
            fd = open(self.adaptee.absolute_path, "wb")
            pickle.dump(obj, fd)
        finally:
            if fd is not None:
                fd.close()

#        self.m_time = getmtime(self.adaptee.absolute_path)


    def load(self):
        """ Load the file """

        fd = None
        try:
            fd = open(self.adaptee.absolute_path, "rb")
            obj = pickle.load(fd)
        finally:
            if fd is not None:
                fd.close()

        return obj

# EOF -------------------------------------------------------------------------
