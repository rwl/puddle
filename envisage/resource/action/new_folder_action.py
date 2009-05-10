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

""" Defines an action for folder resource creation.
"""

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
    """ An action for creating new folders.
    """

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
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action.
        """
        wizard = FolderWizard(parent=self.window.control, window=self.window,
            title="New Folder")

        # Open the wizard
        if wizard.open() == OK:
            wizard.finished = True

        return

# EOF -------------------------------------------------------------------------
