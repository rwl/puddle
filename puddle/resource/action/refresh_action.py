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

""" Defines an action for refreshing a resource.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.io.api import File
from enthought.traits.api import Bool, Instance
from enthought.pyface.action.api import Action
from enthought.pyface.api import ImageResource

from puddle.resource.i_workspace import IWorkspace
from puddle.resource.resource_view import RESOURCE_VIEW

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "RefreshAction" class:
#------------------------------------------------------------------------------

class RefreshAction(Action):
    """ Defines an action for refreshing a resource.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Re&fresh"

    # Keyboard accelerator:
    accelerator = "F5"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("refresh", search_path=[IMAGE_LOCATION])

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        selections = self.window.selection

        if selections:
            selection = selections[0]

            if isinstance(selection, File):
                view = self.window.get_view_by_id(RESOURCE_VIEW)
                if view is not None:
                    view.tree_viewer.refresh(selection)


# EOF -------------------------------------------------------------------------
