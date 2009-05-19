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

""" Defines an action for saving to a new name.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Bool, Instance
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.api import WorkbenchWindow

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "SaveAsAction" class:
#------------------------------------------------------------------------------

class SaveAsAction(Action):
    """ Defines an action that save the contents of the current editor to
        a new name.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Save the active editor's changes to a new file"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Save As..."

    # A short description of the action used for tooltip text etc:
    tooltip = "Save As"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("save_as", search_path=[IMAGE_LOCATION])

    # Is the action enabled?
    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "SaveAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "SaveAction" interface:
    #--------------------------------------------------------------------------

    def _active_editor_changed_for_window(self):
        """ Enables the action if the window has editors.
        """
        if self.window.editors:
            self.enabled = True
        else:
            self.enabled = False

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action.
        """
        active_editor = self.window.active_editor

        if self.enabled and (active_editor is not None):
            active_editor.save_as()

# EOF -------------------------------------------------------------------------
