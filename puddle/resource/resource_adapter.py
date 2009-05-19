#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#  IN THE SOFTWARE.
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
