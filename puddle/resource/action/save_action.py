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

""" Defines an action for saving the contents of the current editor.
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
#  "SaveAction" class:
#------------------------------------------------------------------------------

class SaveAction(Action):
    """ Defines an action that save the contents of the current editor.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Save the active editor's changes"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Save"

    # A short description of the action used for tooltip text etc:
    tooltip = "Save (Ctrl+S)"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("save", search_path=[IMAGE_LOCATION])

    # Keyboard accelerator
    accelerator = "Ctrl+S"

    # Is the action enabled?
    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "SaveAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "SaveAction" interface:
    #--------------------------------------------------------------------------

    def _active_editor_changed_for_window(self, obj, name, old, new):
        """ Sets up static event handlers for change in the clean state
            of the active editor
        """

        if old is not None:
            old.on_trait_change(self.active_editor_dirt, "dirty", remove=True)

        if new is not None:
            new.on_trait_change(self.active_editor_dirt, "dirty")
            self.active_editor_dirt(dirty=new.dirty)


    def active_editor_dirt(self, dirty):
        """ Enables the action if the active editor is dirty.
        """
        if dirty:
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
            active_editor.save()

# EOF -------------------------------------------------------------------------
