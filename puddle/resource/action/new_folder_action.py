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

""" Defines an action for folder resource creation.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.io.api import File
from enthought.traits.api import Bool, on_trait_change
from enthought.pyface.api import ImageResource, OK, error
from enthought.pyface.action.api import Action
from enthought.pyface.wizard.api import SimpleWizard, ChainedWizard

from puddle.resource.wizard.folder_wizard import FolderWizard

from common import IMAGE_LOCATION

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
