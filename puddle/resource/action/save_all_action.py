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

""" Defines an action that save the contents of all dirty editors.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Bool
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "SaveAllAction" class:
#------------------------------------------------------------------------------

class SaveAllAction(Action):
    """ Defines an action that save the contents of all dirty editors.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Save all unsaved changes"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Sav&e All"

    # A short description of the action used for tooltip text etc:
    tooltip = "Save All (Shift+Ctrl+S)"

    # The action's image (displayed on tool bar tools etc):
#    image = ImageResource("save_all", search_path=[IMAGE_LOCATION])

    # Keyboard accelerator
    accelerator = "Shift+Ctrl+S"

    # Is the action enabled?
    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, **traits):
        """ Returns a new SaveAllAction.
        """
        super(SaveAllAction, self).__init__(**traits)

        if traits.has_key("window"):
            traits["window"].on_trait_change(self.on_editors_change,
                "editors_items")

    #--------------------------------------------------------------------------
    #  "SaveAllAction" interface:
    #--------------------------------------------------------------------------

    def on_editors_change(self, event):
        """ Sets up static event handlers for all workbench editors.
        """
        for editor in event.removed:
            editor.on_trait_change(self.on_editor_dirt, "dirty", remove=True)

        for editor in event.added:
            editor.on_trait_change(self.on_editor_dirt, "dirty")

        # Perform an sweep of the editors.
        self.on_editor_dirt(None)


#    @on_trait_change("window.editors.dirty")
    def on_editor_dirt(self, dirty):
        """ Enables the action when any editor is dirty.
        """
        self.enabled = bool([e for e in self.window.editors if e.dirty])

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action.
        """
        for editor in self.window.editors:
            editor.save()

# EOF -------------------------------------------------------------------------
