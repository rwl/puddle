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

""" Defines a workbench tree view of resources.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.io.api import File
from enthought.traits.api import Instance
from enthought.traits.ui.api import View, Item, TreeEditor
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.workbench.api import View as WorkbenchView
from enthought.pyface.action.api import MenuManager, Group

from enthought.envisage.ui.workbench.workbench_action_manager_builder import \
    WorkbenchActionManagerBuilder

from resource_tree_node import FileTreeNode

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"

#------------------------------------------------------------------------------
#  "ResourceTreeView" class:
#------------------------------------------------------------------------------

class ResourceTreeView(WorkbenchView):
    """ Defines a workbench tree view of resources.
    """

    #--------------------------------------------------------------------------
    #  "ResourceTreeView" interface:
    #--------------------------------------------------------------------------

    workspace = Instance(File)

    # A builder for the tree context menu
#    action_manager_builder = Instance(WorkbenchActionManagerBuilder)

    # The tree context menu
    context_menu = Instance(MenuManager)

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    # The view's globally unique identifier:
    id = "puddle.resource.resource_tree_view"

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
        """ Create the view contents.
        """
#        browser = WorkspaceBrowser(window=self.window)
        ui = self.edit_traits(parent=parent, view=self._create_view(),
            kind="subpanel")

        return ui.control

    #--------------------------------------------------------------------------
    #  "ResourceTreeView" interface:
    #--------------------------------------------------------------------------

    def _workspace_default(self):
        """ Trait initialiser.
        """
        # Note that we always offer the service via its name, but look it up
        # via the actual protocol.
        from i_workspace import IWorkspace
        workspace = self.window.application.get_service(IWorkspace)

        return workspace


    def _context_menu_default(self):
        """ Trait initialiser.
        """
        extensions = self.window.application.get_extensions(ACTION_SETS)
        action_sets = [ext(window=self.window) for ext in extensions]

        action_manager_builder = WorkbenchActionManagerBuilder(
            window=self.window, action_sets=action_sets)

        context_menu_manager = MenuManager(
            name="Resource", id="puddle.resource.context_menu")

        action_manager_builder.initialize_action_manager(
            context_menu_manager, "Resource")

        return context_menu_manager


    def _create_view(self):
        """ Create a view with a tree editor.
        """
        view = View(
            Item(
                name="workspace", show_label=False,
                editor=TreeEditor(
                    nodes=[FileTreeNode(menu=self.context_menu)],
                    editable=False, hide_root=True,
                    on_dclick=self._on_dclick,
                    on_select=self._on_select,
                )
            ),
            buttons=["OK", "Cancel"],
            resizable=True,
            width=.3, height=.3
        )

        return view


    def _on_dclick(self, object):
        """ Handle tree nodes being double clicked.
        """
        self.window.edit(object)


    def _on_select(self, object):
        """ Handle tree node selection.
        """
        pass

# EOF -------------------------------------------------------------------------
