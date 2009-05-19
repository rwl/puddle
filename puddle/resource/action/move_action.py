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

""" Defines an action for moving resources.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import dirname, join

from enthought.io.api import File
from enthought.traits.api import HasTraits, Directory, Bool, Instance
from enthought.traits.ui.api import View, Item, Label
from enthought.pyface.api import ImageResource, confirm, YES
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.resource_view import RESOURCE_VIEW

#------------------------------------------------------------------------------
#  "DirectorySelection" class:
#------------------------------------------------------------------------------

class DirectorySelection(HasTraits):
    """ Defines a dialog for the destination selection.
    """
    directory = Directory

    traits_view = View(
        Label("Enter or select the directory:"),
        Item(name="directory", style="text", show_label=False),
        Item(name="directory", style="custom", show_label=False),
        title="Directory Selection", buttons=["OK", "Cancel"],
        width=0.3, resizable=True)

#------------------------------------------------------------------------------
#  "MoveAction" class:
#------------------------------------------------------------------------------

class MoveAction(Action):
    """ Defines an action for moving resources.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Move the selected resource"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Mo&ve..."

    # A short description of the action used for tooltip text etc:
    tooltip = "Move resource"

    #--------------------------------------------------------------------------
    #  "RenameAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "RenameAction" interface:
    #--------------------------------------------------------------------------

    def _selection_changed_for_window(self, selections):
        """ Enables the action if the window has editors.
        """
        self.enabled = self._is_enabled(selections)


    def _enabled_default(self):
        """ Trait initialiser.
        """
        selections = self.window.selection

        return self._is_enabled(selections)


    def _is_enabled(self, selections):
        """ Returns true if the action should be enabled.
        """
        if selections and isinstance(selections[0], File):
            return True
        else:
            return False

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        selection = self.window.selection[0]

        ds = DirectorySelection(directory=dirname(selection.absolute_path))

        retval = ds.edit_traits(parent=self.window.control, kind="livemodal")

        if retval.result:
            destination = join(ds.directory, selection.name+selection.ext)
            selection.move(destination)

            # Refresh the workspace tree view
            view = self.window.get_view_by_id(RESOURCE_VIEW)
            if view is not None:
                # Note that we always offer the service via its name, but look
                # it up via the actual protocol.
                from puddle.resource.i_workspace import IWorkspace
                workspace = self.window.application.get_service(IWorkspace)
                # Refresh the parent directory and not the whole tree
                view.tree_viewer.refresh(workspace)

# EOF -------------------------------------------------------------------------
