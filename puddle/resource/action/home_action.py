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

""" Defines an action for moving the workspace to the user's home directory.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser

from enthought.traits.api import Bool, Instance
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.resource_view import RESOURCE_VIEW

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "HomeAction" class:
#------------------------------------------------------------------------------

class HomeAction(Action):
    """ An action for moving the workspace to the user's home directory.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Move workspace to the user's home directory"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Home"

    # A short description of the action used for tooltip text etc:
    tooltip = "Open home directory"

    # Keyboard accelerator:
    accelerator = "Alt+Home"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("home_folder", search_path=[IMAGE_LOCATION])

    #--------------------------------------------------------------------------
    #  "UpAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        # Note that we always offer the service via its name, but look it up
        # via the actual protocol.
        from puddle.resource.i_workspace import IWorkspace

        workspace = self.window.application.get_service(IWorkspace)
        workspace.path = expanduser("~")

        view = self.window.get_view_by_id(RESOURCE_VIEW)
        if view is not None:
            view.tree_viewer.refresh(workspace)

# EOF -------------------------------------------------------------------------
