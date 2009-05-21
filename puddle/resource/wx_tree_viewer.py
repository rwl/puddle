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

""" Defines a resource tree viewer.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.pyface.viewer.api import TreeViewer as WxTreeViewer

#------------------------------------------------------------------------------
#  "TreeViewer" class:
#------------------------------------------------------------------------------

class TreeViewer(WxTreeViewer):
    """ A viewer based on a WX tree widget.
    """

    #--------------------------------------------------------------------------
    #  "TreeViewer" interface
    #--------------------------------------------------------------------------

    def refresh(self, element):#=None):
        """ Refresh the tree starting from the specified element.

            Call this when the STRUCTURE of the content has changed.
        """
        # Refresh from the root if no element specified
#        if element is None:
#            pid = self.control.GetRootItem()
#            data = self.control.GetPyData(pid)
#            if data is not None:
#                populated, element = data

        # Has the element actually appeared in the tree yet?
        pid = self._element_to_id_map.get(self._get_key(element), None)
        if pid is not None:
            # The item data is a tuple.  The first element indicates whether or
            # not we have already populated the item with its children.  The
            # second element is the actual item data.
            populated, element = self.control.GetPyData(pid)#

            # If an element is expanded and is not collapsed before we continue
            # then the pizza slice points down, but no children are displayed.
            # The node then has to be manually collapsed and then expanded.
            self.control.Collapse(pid)

            # fixme: We should find a cleaner way other than deleting all of
            # the element's children and re-adding them!
            self._delete_children(pid)
            self.control.SetPyData(pid, (False, element))

            # Does the element have any children?
            has_children = self.content_provider.has_children(element)
            self.control.SetItemHasChildren(pid, has_children)

            # Expand it.
            self.control.Expand(pid)

        else:
            print '**** pid is None!!! ****'

        return


    def _delete_children(self, pid):
        """ Recursively deletes the children of the specified element.
        """
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

    #--------------------------------------------------------------------------
    #  Trait event handlers:
    #--------------------------------------------------------------------------

    def _element_right_clicked_changed(self, event):
        """ Forces selection of the item under the cursor on right click.
        """
        element, point = event

        wx_item, flags = self.control.HitTest(point)
        self.control.SelectItem(wx_item)

# EOF -------------------------------------------------------------------------
