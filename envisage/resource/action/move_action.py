#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
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

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

WORKSPACE_VIEW = "envisage.resource.resource_view"

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
            view = self.window.get_view_by_id(WORKSPACE_VIEW)
            if view is not None:
                # Note that we always offer the service via its name, but look
                # it up via the actual protocol.
                from envisage.resource.i_workspace import IWorkspace
                workspace = self.window.application.get_service(IWorkspace)
                # Refresh the parent directory and not the whole tree
                view.tree_viewer.refresh(workspace)

# EOF -------------------------------------------------------------------------
