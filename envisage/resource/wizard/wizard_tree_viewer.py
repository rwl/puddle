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

""" Defines a workspace tree viewer """

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Instance

from enthought.pyface.viewer.api import \
    TreeContentProvider, TreeLabelProvider, TreeViewer

#------------------------------------------------------------------------------
#  "WizardTreeContentProvider" class:
#------------------------------------------------------------------------------

class WizardTreeContentProvider(TreeContentProvider):
    """ Defines a wizard tree content provider """

    #--------------------------------------------------------------------------
    #  "TreeContentProvider" interface.
    #--------------------------------------------------------------------------

    def get_parent(self, element):
        """ Returns the parent of an element. """

        return None


    def get_children(self, element):
        """ Returns the children of an element. """

        if hasattr(element, "wizards"):
            return element.wizards
        else:
            return []


    def has_children(self, element):
        """ Returns True iff the element has children, otherwise False. """

        if hasattr(element, "wizards"):
            return bool(element.wizards)
        else:
            return False

#------------------------------------------------------------------------------
#  "WizardTreeLabelProvider" class:
#------------------------------------------------------------------------------

class WizardTreeLabelProvider(TreeLabelProvider):
    """ Defines a workspace tree label provider """

    #--------------------------------------------------------------------------
    #  "TreeLabelProvider" interface
    #--------------------------------------------------------------------------

    def get_image(self, viewer, element):
        """ Returns the filename of the label image for an element. """

        if hasattr(element, "image"):
            return element.image
        else:
            return None


    def get_text(self, viewer, element):
        """ Returns the label text for an element. """

        return element.name

#------------------------------------------------------------------------------
#  "WizardTreeViewer" class:
#------------------------------------------------------------------------------

class WizardTreeViewer(TreeViewer):
    """ A tree viewer for a list of wizards """

    #--------------------------------------------------------------------------
    #  "TreeViewer" interface
    #--------------------------------------------------------------------------

    # The content provider provides the actual tree data.
    content_provider = Instance(WizardTreeContentProvider, ())

    # The label provider provides, err, the labels for the items in the tree
    # (a label can have text and/or an image).
    label_provider = Instance(WizardTreeLabelProvider, ())

    # Selection mode (must be either of 'single' or 'extended').
    selection_mode = "single"

    # Should the root of the tree be shown?
    show_root = True

    def _delete_children(self, pid):
        """ Recursively deletes the children of the specified element. """

        cookie = 0

#        (cid, cookie) = self.control.GetFirstChild(pid, cookie) # Obsolete
        (cid, cookie) = self.control.GetFirstChild(pid)
        while cid.IsOk():
            # Recursively delete the child's children.
            self._delete_children(cid)

            # Remove the reference to the item's data.
            populated, element = self.control.GetPyData(cid)
            del self._element_to_id_map[self._get_key(element)]
            self.control.SetPyData(cid, None)

            # Next!
            (cid, cookie) = self.control.GetNextChild(pid, cookie)

        self.control.DeleteChildren(pid)

        return

# EOF -------------------------------------------------------------------------
