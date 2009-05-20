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

""" Defines a tree view of resources for the workbench.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import wx

from enthought.traits.api import Instance, Delegate
from enthought.pyface.action.api import MenuManager, Group
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.workbench.api import View as WorkbenchView

from enthought.envisage.ui.workbench.workbench_action_manager_builder import \
    WorkbenchActionManagerBuilder

#from resource import File
from enthought.io.api import File

from action.open_action import OpenAction

from resource_tree_viewer import \
    ResourceTreeViewer, FileSorter, ResourceTreeLabelProvider, \
    HideHiddenFiles

#from enthought.pyface.action.api import ToolBarManager, Action

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

RESOURCE_VIEW = "puddle.resource.resource_view"

ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"

#------------------------------------------------------------------------------
#  "ResourceView" class:
#------------------------------------------------------------------------------

class ResourceView(WorkbenchView):
    """ Defines a tree view of resources for the workbench.
    """

    #--------------------------------------------------------------------------
    #  "WorkspaceView" interface:
    #--------------------------------------------------------------------------

    # A view of resources based on a tree control
    tree_viewer = Instance(ResourceTreeViewer)

    # That which is currently selected in the tree
    selection = Delegate("tree_viewer")

    # A builder for the tree context menu
    action_manager_builder = Instance(WorkbenchActionManagerBuilder)

    # The tree context menu
    context_menu = Instance(MenuManager)

    # A tree label provider that uses contributed editor icons
    label_provider = Instance(ResourceTreeLabelProvider)

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    # The view's globally unique identifier:
    id = RESOURCE_VIEW

    # The view's name:
    name = "Navigator"

    # The default position of the view relative to the item specified in the
    # "relative_to" trait:
    position = "left"

    # An image used to represent the view to the user (shown in the view tab
    # and in the view chooser etc).
    image = ImageResource("tree")

    # The width of the item (as a fraction of the window width):
    width = 0.2

    # The category sed to group views when they are displayed to the user:
    category = "General"

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    def create_control(self, parent):
        """ Create the view contents """

        # Note that we always offer the service via its name, but look it up
        # via the actual protocol.
        from i_workspace import IWorkspace

        workspace = self.window.application.get_service(IWorkspace)

        # Create a tree viewer with the workspace as input
        self.tree_viewer = tree_viewer = ResourceTreeViewer(
            parent, input=workspace,
            label_provider=self.label_provider,
            sorter=FileSorter(),
            filters=[HideHiddenFiles()]
        )

        # Make the TreeViewer a selection provider
        tree_viewer.on_trait_change(self.on_selection_change, "selection")
        # Add a right-click handler for showing the context menu
        tree_viewer.on_trait_change(
            self.on_right_click, "element_right_clicked"
        )
        # Add a double-click handler for opening resources
        tree_viewer.on_trait_change(self.on_double_click, "element_activated")

        tree_viewer.on_trait_change(self.on_key, "key_pressed")

        return tree_viewer.control

    #--------------------------------------------------------------------------
    #  "ResourceView" interface:
    #--------------------------------------------------------------------------

    def _label_provider_default(self):
        """ Trait initialiser """

        return ResourceTreeLabelProvider(window=self.window)


    def _action_manager_builder_default(self):
        """ Trait initialiser """

        extensions = self.window.application.get_extensions(ACTION_SETS)
        action_sets = [factory(window=self.window) for factory in extensions]

        action_manager_builder = WorkbenchActionManagerBuilder(
            window=self.window, action_sets=action_sets
        )

        return action_manager_builder


    def _context_menu_default(self):
        """ Trait initialiser """

        context_menu_manager = MenuManager(
            name="Resource", id="puddle.resource.context_menu"
        )

        self.action_manager_builder.initialize_action_manager(
            context_menu_manager, "Resource"
        )

        return context_menu_manager


    def on_selection_change(self, new):
        """ Sets the workbench window's currently selected item """

        self.window.selection = new


    def on_right_click(self, event):
        """ Handles displaying the context menu on right-click """

        element, (x, y) = event
        parent = self.tree_viewer.control
        self.context_menu.create_menu(parent).show(x, y)


    def on_double_click(self, element):
        """ Opens a file resource in the default editor """

        if element.is_file:
            self._open_selection()
        elif element.is_folder:
            self._change_workspace(element)
        else:
            pass


    def on_key(self, key_code):
        """ Handles key presses when the tree is active.
        """
        window = self.window
        viewer = self.tree_viewer

        if viewer.selection:
            selected = viewer.selection[0]
        else:
            return

        if key_code == wx.WXK_RETURN:
            if selected.is_file:
                self._open_selection()
            elif selected.is_folder:
                self._change_workspace(selected)

        elif key_code == wx.WXK_SPACE:
            if selected.is_file:
                self._open_selection()
            elif selected.is_folder:
                item_id = viewer.control.GetSelection()
                if viewer.control.IsExpanded(item_id):
                    viewer.control.Collapse(item_id)
                else:
                    viewer.control.Expand(item_id)

        elif key_code == wx.WXK_DOWN:
            item_id = viewer.control.GetSelection()
            next = viewer.control.GetNextVisible(item_id)
            viewer.control.SelectItem(next)

        elif key_code == wx.WXK_UP:
            item_id = viewer.control.GetSelection()
            prev = viewer.control.GetPrevSibling(item_id)
            viewer.control.SelectItem(prev)

        elif key_code == wx.WXK_PAGEDOWN:
            item_id = viewer.control.GetSelection()

            if viewer.control.IsExpanded(item_id):
                sibling = viewer.control.GetNextSibling(item_id)
            else:
                parent = viewer.control.GetItemParent(item_id)
                sibling = viewer.control.GetNextSibling(parent)

            viewer.control.SelectItem(sibling)

        elif key_code == wx.WXK_PAGEUP:
            item_id = viewer.control.GetSelection()
            prev = viewer.control.GetItemParent(item_id)
            viewer.control.SelectItem(prev)

        else:
            pass


    def _open_selection(self):
        window = self.window
        viewer = self.tree_viewer

        if viewer.selection:
            selected = viewer.selection[0]
        else:
            return

        OpenAction(window=window).perform(None)
        window.selection = viewer.selection


    def _change_workspace(self, element):
        from i_workspace import IWorkspace
        workspace = self.window.application.get_service(IWorkspace)
        workspace.path = element.absolute_path

        self.tree_viewer.refresh(workspace)

# EOF -------------------------------------------------------------------------
