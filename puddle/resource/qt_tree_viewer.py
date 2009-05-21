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

""" A viewer based on a PyQT4 tree control.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from PyQt4 import QtCore, QtGui

#from enthought.pyface.image_list import ImageList
from enthought.traits.api import Any, Bool, Enum, Event, Instance, List
#from enthought.util.wx.drag_and_drop import PythonDropSource

from enthought.pyface.viewer.content_viewer import ContentViewer
from enthought.pyface.viewer.tree_content_provider import TreeContentProvider
from enthought.pyface.viewer.tree_label_provider import TreeLabelProvider

#------------------------------------------------------------------------------
#  "TreeViewer" class:
#------------------------------------------------------------------------------

class TreeViewer(ContentViewer):
    """ A viewer based on a PyQT4 tree control.
    """

    #--------------------------------------------------------------------------
    #  'TreeViewer' interface
    #--------------------------------------------------------------------------

    # The content provider provides the actual tree data.
    content_provider = Instance(TreeContentProvider)

    # The label provider provides, err, the labels for the items in the tree
    # (a label can have text and/or an image).
    label_provider = Instance(TreeLabelProvider, ())

    # Selection mode (must be either of 'single' or 'extended').
    selection_mode = Enum('single', 'extended')

    # The currently selected elements.
    selection = List

    # Should an image be shown for each element?
    show_images = Bool(True)

    # Should the root of the tree be shown?
    show_root = Bool(True)

    #### Events ####

    # An element has been activated (ie. double-clicked).
    element_activated = Event

    # A drag operation was started on an element.
    element_begin_drag = Event

    # An element that has children has been collapsed.
    element_collapsed = Event

    # An element that has children has been expanded.
    element_expanded = Event

    # A left-click occurred on an element.
    element_left_clicked = Event

    # A right-click occurred on an element.
    element_right_clicked = Event

    # A key was pressed while the tree is in focus.
    key_pressed = Event

    #--------------------------------------------------------------------------
    #  'object' interface.
    #--------------------------------------------------------------------------

    def __init__(self, parent, image_size=(16, 16), **traits):
        """ Creates a new tree viewer.

            'parent' is the toolkit-specific control that is the tree's parent.

            'image_size' is a tuple in the form (int width, int height) that
            specifies the size of the images (if any) displayed in the tree.
        """
        # Base class constructor.
        super(TreeViewer, self).__init__(**traits)

        # Create the toolkit-specific control.
        self.control = tree = QtGui.QTreeWidget(parent)

        tree.setColumnCount(1)
        tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header = tree.headerItem()
        header.setHidden(True)

        # Get our actual Id.
#        wxid = tree.GetId()

        # Wire up the wx tree events.
#        wx.EVT_CHAR(tree, self._on_char)
#        wx.EVT_LEFT_DOWN(tree, self._on_left_down)
        tree.connect(tree,
            QtCore.SIGNAL('itemClicked(QTreeWidgetItem *, int)'),
            self._on_left_down)
#        wx.EVT_RIGHT_DOWN(tree, self._on_right_down)
        tree.connect(tree,
            QtCore.SIGNAL('customContextMenuRequested(QPoint)'),
            self._on_right_down)
#        wx.EVT_TREE_ITEM_ACTIVATED(tree, wxid, self._on_tree_item_activated)
        tree.connect(tree,
            QtCore.SIGNAL('itemDoubleClicked(QTreeWidgetItem *, int)'),
            self._on_tree_item_activated)
#        wx.EVT_TREE_ITEM_COLLAPSED(tree, wxid, self._on_tree_item_collapsed)
        tree.connect(tree,
            QtCore.SIGNAL('itemCollapsed(QTreeWidgetItem *)'),
            self._on_tree_item_collapsed)
#        wx.EVT_TREE_ITEM_COLLAPSING(tree, wxid, self._on_tree_item_collapsing)
#        wx.EVT_TREE_ITEM_EXPANDED(tree, wxid, self._on_tree_item_expanded)
        tree.connect(tree,
            QtCore.SIGNAL('itemExpanded(QTreeWidgetItem *)'),
            self._on_tree_item_expanded)
#        wx.EVT_TREE_ITEM_EXPANDING(tree, wxid, self._on_tree_item_expanding)
#        wx.EVT_TREE_BEGIN_LABEL_EDIT(tree, wxid,self._on_tree_begin_label_edit)
#        wx.EVT_TREE_END_LABEL_EDIT(tree, wxid, self._on_tree_end_label_edit)
#        wx.EVT_TREE_BEGIN_DRAG(tree, wxid, self._on_tree_begin_drag)
#        wx.EVT_TREE_SEL_CHANGED(tree, wxid, self._on_tree_sel_changed)
        tree.connect(tree,
            QtCore.SIGNAL('itemSelectionChanged()'),
            self._on_tree_sel_changed)

        # The image list is a wxPython-ism that caches all images used in the
        # control.
#        self._image_list = ImageList(image_size[0], image_size[1])
#        if self.show_images:
#            tree.AssignImageList(self._image_list)

        # Mapping from element to wx tree item Ids.
        self._element_to_id_map = {}

        # Add the root item.
        if self.input is not None:
            self._add_element(None, self.input)

        return

    #--------------------------------------------------------------------------
    #  'TreeViewer' interface.
    #--------------------------------------------------------------------------

    def is_expanded(self, element):
        """ Returns True if the element is expanded, otherwise False.
        """
        key = self._get_key(element)

        if key in self._element_to_id_map:
            nid = self._element_to_id_map[key]
            is_expanded = nid.isExpanded()

        else:
            is_expanded = False

        return is_expanded


    def is_selected(self, element):
        """ Returns True if the element is selected, otherwise False.
        """
        key = self._get_key(element)

        if key in self._element_to_id_map:
            nid = self._element_to_id_map[key]
            is_selected = nid.isSelected()

        else:
            is_selected = False

        return is_selected


    def refresh(self, element):
        """ Refresh the tree starting from the specified element.

            Call this when the STRUCTURE of the content has changed.
        """
        # Has the element actually appeared in the tree yet?
        key = self._get_key(element)
        pid = self._element_to_id_map.get(key, None)

        if pid is not None:
            # The item data is a tuple.  The first element indicates whether or
            # not we have already populated the item with its children.  The
            # second element is the actual item data.
            populated, element = self._get_node_data(pid)

            # fixme: We should find a cleaner way other than deleting all of
            # the element's children and re-adding them!
            self._delete_children(pid)
            self._set_node_data(pid, (False, element))

            # Does the element have any children?
#            has_children = self.content_provider.has_children(element)
#            self.control.SetItemHasChildren(pid, has_children)

            # Expand it.
            pid.setExpanded(True)

        else:
            print '**** pid is None!!! ****'

        return


    def update(self, element):
        """ Update the tree starting from the specified element.

            Call this when the APPEARANCE of the content has changed.
        """
        key = self._get_key(element)
        pid = self._element_to_id_map.get(key, None)

        if pid is not None:
            self._refresh_element(pid, element)

            for child in self.content_provider.get_children(element):
                ckey = self._get_key(child)
                cid = self._element_to_id_map.get(ckey, None)
                if cid is not None:
                    self._refresh_element(cid, child)

        return

    #--------------------------------------------------------------------------
    #  Private interface:
    #--------------------------------------------------------------------------

    def _add_element(self, pid, element):
        """ Adds 'element' as a child of the element identified by 'pid'.

            If 'pid' is None then we are adding the root element.
        """
        tree = self.control

        # Get the tree item image index and text.
#        image_index = self._get_image_index(element)
        image = self.label_provider.get_image(self, element)
        text = self._get_text(element)

        # Add the element.
        if pid is None:
            nid = QtGui.QTreeWidgetItem(tree, [text])
            nid.setIcon(0, image.create_icon())

        else:
            nid = QtGui.QTreeWidgetItem(pid, [text])
            nid.setIcon(0, image.create_icon())

        # If we are adding the root element but the root is hidden, get its
        # children.
        if pid is None and not self.show_root:
            children = self.content_provider.get_children(element)
            for child in children:
                self._add_element(nid, child)

        # Does the element have any children?
        if self.content_provider.has_children(element):
            # Qt only draws the control that expands the tree if there is a
            # child.  As the tree is being populated lazily we create a
            # dummy that will be removed when the node is expanded for the
            # first time.
            nid._dummy = QtGui.QTreeWidgetItem(nid, ["dummy"])


        # The item data is a tuple. The first element indicates whether or not
        # we have already populated the item with its children. The second
        # element is the actual item data.
        if pid is None:
            if self.show_root:
                self._set_node_data(nid, (False, element))

        else:
            self._set_node_data(nid, (False, element))

        # Make sure that we can find the element's Id later.
        self._element_to_id_map[self._get_key(element)] = nid

        # If we are adding the root item then automatically expand it.
        if pid is None and self.show_root:
            nid.setExpanded(True)

        return


    def _get_key(self, element):
        """ Generate the key for the element to id map.
        """
        try:
            key = hash(element)

        except:
            key = id(element)

        return key


    def _get_text(self, element):
        """ Returns the tree item text for an element.
        """
        text = self.label_provider.get_text(self, element)

        if text is None:
            text = ''

        return text


    def _refresh_element(self, nid, element):
        """ Refreshes the image and text of the specified element.
        """
        # Get the tree item image index.
#        image_index = self._get_image_index(element)
        image = self.label_provider.get_image(self, element)

        nid.setIcon(0, image.create_icon())

        # Get the tree item text.
        text = self._get_text(element)
        nid.setText(0, text)

        return


#    def _unpack_event(self, event):
#        """ Unpacks the event to see whether a tree element was involved.
#        """
#        try:
#            point = event.pos()
#
#        except:
#            point = event.globalPos()
#
#        nid = self.control.itemAt(point)
#        data = self._get_node_data(nid)
#
#        return data, nid, point


    def _get_selection(self):
        """ Returns a list of the selected elements.
        """
        elements = []
        for nid in self.control.selectedItems():
            data = self._get_node_data(nid)
            if data is not None:
                populated, element = data
                elements.append(element)

        return elements


    def _delete_children(self, pid):
        """ Recursively deletes the children of the specified element.
        """
        cid = pid.child(0)

        for cidx in range(cid.childCount()):
            # Recursively delete the child's children.
            self._delete_children(cid)

            # Remove the reference to the item's data.
            populated, element = self._get_node_data(cid)
            del self._element_to_id_map[self._get_key(element)]
            self._set_node_data(cid, None)

            cid.removeChild(cidx)


        return

    #---------------------------------------------------------------------------
    #  Gets/Sets the node specific data:
    #---------------------------------------------------------------------------

    @staticmethod
    def _get_node_data(nid):
        """ Gets the node specific data.
        """
        return nid._py_data


    @staticmethod
    def _set_node_data(nid, data):
        """ Sets the node specific data.
        """
        nid._py_data = data

    #--------------------------------------------------------------------------
    #  Trait event handlers:
    #--------------------------------------------------------------------------

    def _input_changed(self):
        """ Called when the tree's input has been changed.
        """
        # Delete everything...
        if self.control is not None:
            self.control.clear()

            self._element_to_id_map = {}

            # ... and then add the root item back in.
            if self.input is not None:
                self._add_element(None, self.input)

        return


#    def _element_begin_drag_changed(self, element):
#        """ Called when a drag is started on a element.
#        """
#        # We ask the label provider for the actual value to drag.
#        drag_value = self.label_provider.get_drag_value(self, element)
#
#        # Start the drag.
#        PythonDropSource(self.control, drag_value)
#
#        return

    #--------------------------------------------------------------------------
    #  Qt event handlers:
    #--------------------------------------------------------------------------

    def _on_right_down(self, event):
        """ Called when the right mouse button is clicked on the tree.
        """
#        data, nid, point = self._unpack_event(event)
        point = event
        nid = self.control.itemAt(point)
        data = self._get_node_data(nid)

        # Did the right click occur on a tree item?
        if data is not None:
            populated, element = data

            # Trait notification.
            self.element_right_clicked = (element, (point.x(), point.y()))

        # Give other event handlers a chance.
#        event.ignore()

        return


    def _on_left_down(self, event):
        """ Called when the left mouse button is clicked on the tree.
        """
#        data, nid, point = self._unpack_event(event)
        nid = event
        data = self._get_node_data(nid)

        point = None

        # Did the left click occur on a tree item?
        if data is not None:
            populated, element = data

            # Trait notification.
            self.element_left_clicked = (element, point)

        # Give other event handlers a chance.
#        event.ignore()

        return


    def _on_tree_item_expanded(self, event):
        """ Called when a tree item is about to expand.
        """
        # Which item is expanding?
        nid = event

        # The item data is a tuple. The first element indicates whether or not
        # we have already populated the item with its children.  The second
        # element is the actual item data.
        populated, element = self._get_node_data(nid)

        # Lazily populate the item's children.
        if not populated:
            children = self.content_provider.get_children(element)

            # Sorting...
            if self.sorter is not None:
                self.sorter.sort(self, element, children)

            # Filtering....
            for child in children:
                for filter in self.filters:
                    if not filter.select(self, element, child):
                        break

                else:
                    self._add_element(nid, child)

            # The element is now populated!
            self._set_node_data(nid, (True, element))

        # Remove any dummy node.
        dummy = getattr(nid, '_dummy', None)
        if dummy is not None:
            nid.removeChild(dummy)
            del nid._dummy

        # The item data is a tuple.  The first element indicates whether or not
        # we have already populated the item with its children.  The second
        # element is the actual item data.
        populated, element = self._get_node_data(nid)

        # Make sure that the element's 'open' icon is displayed etc.
        self._refresh_element(nid, element)

        # Trait notification.
        self.element_expanded = element


    def _on_tree_item_collapsed(self, event):
        """ Called when a tree item has been collapsed.
        """
        # Which item was collapsed?
        nid = event

        # The item data is a tuple.  The first element indicates whether or not
        # we have already populated the item with its children.  The second
        # element is the actual item data.
        populated, element = self._get_node_data(nid)

        # Make sure that the element's 'closed' icon is displayed etc.
        self._refresh_element(nid, element)

        # Trait notification.
        self.element_collapsed = element

        return


    def _on_tree_item_activated(self, event):
        """ Called when a tree item is activated (i.e., double clicked).
        """
        # Which item was activated?
        nid = event

        # The item data is a tuple.  The first element indicates whether or not
        # we have already populated the item with its children.  The second
        # element is the actual item data.
        populated, element = self._get_node_data(nid)

        # Trait notification.
        self.element_activated = element

        return


    def _on_tree_sel_changed(self):
        """ Called when the selection is changed.
        """
        # Trait notification.
        self.selection = self._get_selection()

        return


#    def _on_tree_begin_drag(self, event):
#        """ Called when a drag operation is starting on a tree item.
#        """
#        # Get the element, its id and the point where the event occurred.
#        data, wxid, flags, point = self._unpack_event(event)
#
#        if point == (0,0):
#            # Apply workaround.
#            point = self._point_left_clicked
#            wxid, flags = self.control.HitTest(point)
#            data = self.control.GetPyData(wxid)
#
#        if data is not None:
#            populated, element = data
#
#            # Trait notification.
#            self.element_begin_drag = element
#
#        return


#    def _on_tree_begin_label_edit(self, event):
#        """ Called when the user has started editing an item's label.
#        """
#        wxid = event.GetItem()
#
#        # The item data is a tuple.  The first element indicates whether or not
#        # we have already populated the item with its children.  The second
#        # element is the actual item data.
#        populated, element = self.control.GetPyData(wxid)
#
#        # Give the label provider a chance to veto the edit.
#        if not self.label_provider.is_editable(self, element):
#            event.Veto()
#
#        return


#    def _on_tree_end_label_edit(self, event):
#        """ Called when the user has finished editing an item's label.
#        """
#        wxid = event.GetItem()
#
#        # The item data is a tuple.  The first element indicates whether or not
#        # we have already populated the item with its children. The second
#        # element is the actual item data.
#        populated, element = self.control.GetPyData(wxid)
#
#        # Give the label provider a chance to veto the edit.
#        label = event.GetLabel()
#        if not self.label_provider.set_text(self, element, label):
#            event.Veto()
#
#        return


#    def _on_char(self, event):
#        """ Called when a key is pressed when the tree has focus.
#        """
#        # Trait notification.
#        self.key_pressed = event.GetKeyCode()
#
#        return

# EOF -------------------------------------------------------------------------
