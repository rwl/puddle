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

""" Defines an action for folder resource creation """

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os import mkdir
from os.path import join, dirname

from enthought.io.api import File
from enthought.traits.api import Bool, on_trait_change
from enthought.pyface.api import ImageResource, OK, error
from enthought.pyface.action.api import Action
from enthought.pyface.wizard.api import SimpleWizard, ChainedWizard

from envisage.resource.wizard.folder_wizard import FolderWizard

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

IMAGE_LOCATION = join(dirname(__file__), "..", "images")

WORKSPACE_VIEW = "pylon.plugin.resource.resource_view"

#------------------------------------------------------------------------------
#  "NewFolderAction" class:
#------------------------------------------------------------------------------

class NewFolderAction(Action):
    """ An action for creating new folders """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Create a new folder resource"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Folder"

    # A short description of the action used for tooltip text etc:
    tooltip = "Create a Folder"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("closed_folder", search_path=[IMAGE_LOCATION])

    # Is the action enabled?
#    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "NewProjectAction" interface:
    #--------------------------------------------------------------------------

#    def __init__(self, **traits):
#        """ Returns a new NewFolderAction """
#        super(NewFolderAction, self).__init__(**traits)
#
#        if traits.has_key("window"):
#            traits["window"].on_trait_change(
#                self.on_selection_change, "selection"
#            )
#
#
#    def on_selection_change(self, new):
#        """ Enables the action if the current selection is a project or
#        a folder and not a workspace.
#
#        """
#
#        if len(new) == 1:
#            selection = new[0]
#            if isinstance(selection, Project):
#                self.enabled = True
#            elif isinstance(selection, File) and selection.is_folder and \
#                (not isinstance(selection, Workspace)):
#                self.enabled = True
#            else:
#                self.enabled = False

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action """

        wizard = FolderWizard(
            parent=self.window.control, window=self.window,
            title="New Folder"
        )

        # Open the wizard
        if wizard.open() == OK:
            pass
            wizard.finished = True

#        workspace = self.window.application.get_service(WORKSPACE_SERVICE)
#        if workspace is not None:
##            selections = self.window.selection
##            print "SELECTIONS:", selections
##            if selections:
##                sel = selections[0]
#
#            cswp = ContainerSelectionWizardPage(
#                id="parent_folder", workspace=workspace
#            )
#            fwp = FolderWizardPage(id="new_folder", cswp=cswp)
#
#            wizard = SimpleWizard(
#                parent=self.window.control,
#                title="New Folder", pages=[cswp, fwp]
#            )
#
#            # Open the wizard
#            if wizard.open() == OK:
#                try:
##                    File(fwp.abs_path).create_folder()
#                    raise NotImplementedError
#                except ValueError:
#                    error(
#                        self.window.control, title="Error",
#                        message="An error was encountered trying to "
#                        "create the folder."
#                    )
#
#                # Refresh the workspace tree view
#                view = self.window.get_view_by_id(WORKSPACE_VIEW)
#                if view is not None:
#                    view.ws_tree_viewer.refresh()
        return

# EOF -------------------------------------------------------------------------
