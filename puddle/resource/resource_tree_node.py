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

""" Defines a tree node for file objects.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import os
import stat

from os.path import basename

from enthought.io.api import File

from enthought.traits.api import HasTraits, Str, List, Instance, Float

from enthought.traits.ui.api import \
    TreeEditor, TreeNode, View, Item, VSplit, HGroup, Handler, Group

#------------------------------------------------------------------------------
#  "FileTreeNode" class:
#------------------------------------------------------------------------------

class FileTreeNode(TreeNode):
    """ A tree node for a file object.
    """

    #--------------------------------------------------------------------------
    # "TreeNode" interface:
    #--------------------------------------------------------------------------

    def allows_children(self, obj):
        """ Return True if this object allows children.
        """
        if obj.is_folder:
            return True
        else:
            return False


    def has_children(self, obj):
        """ Returns True if this object has children.
        """
        return bool(obj.children)


    def get_children(self, obj):
        """ Get the object's children
        """
        folders = [file for file in obj.children if file.is_folder]
        files = [file for file in obj.children if file.is_file]

        shown = [file for file in folders+files if not
            basename(file.absolute_path).startswith(".")]

        return shown


    def get_label(self, obj):
        """ Get the object's label.
        """
        return obj.name+obj.ext


    def is_node_for(self, obj):
        """ Return whether this is the node for a specified object.
        """
        return isinstance(obj, File)


    def get_view(self, object):
        """ Gets the view to use when editing an object.
        """
        view = View(Item(name="absolute_path", style="readonly"),
            Item(name="mime_type", style="readonly"),
            Item(name="url", style="readonly"))

        return view


#    def get_icon ( self, object, is_expanded ):
#        """ Returns the icon for a specified object """
#
#        if not self.allows_children( object ):
#            return self.icon_item
#
#        if is_expanded:
#            return self.icon_open
#
#        return self.icon_group
#
#
#    def get_icon_path ( self, object ):
#        """ Returns the path used to locate an object's icon """
#
#        return self.icon_path

# EOF -------------------------------------------------------------------------
