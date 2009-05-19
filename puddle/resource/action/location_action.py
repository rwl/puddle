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

""" Defines an action for moving the workspace to a new location.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser

from enthought.traits.api import Bool, Instance
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from move_action import DirectorySelection

from puddle.resource.resource_view import RESOURCE_VIEW

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

IMAGE_LOCATION = join( dirname(__file__), "..", "images" )

#------------------------------------------------------------------------------
#  "LocationAction" class:
#------------------------------------------------------------------------------

class LocationAction(Action):
    """ An action for moving the workspace to a new location.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Move the workspace to a new location"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Location..."

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("location", search_path=[IMAGE_LOCATION])

    # A short description of the action used for tooltip text etc:
    tooltip = "Move workspace location"

    # Keyboard accelerator:
    accelerator = "Ctrl+L"

    #--------------------------------------------------------------------------
    #  "LocationAction" interface:
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

        ds = DirectorySelection(directory=dirname(workspace.absolute_path))

        retval = ds.edit_traits(parent=self.window.control, kind="livemodal")

        if retval.result:
            workspace.path = ds.directory

            # Refresh the workspace tree view
            view = self.window.get_view_by_id(RESOURCE_VIEW)
            if view is not None:
                view.tree_viewer.refresh(workspace)

# EOF -------------------------------------------------------------------------
