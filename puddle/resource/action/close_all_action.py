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

""" Defines an action for closing all editors.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Bool
from enthought.pyface.action.api import Action

#------------------------------------------------------------------------------
#  "CloseAllAction" class:
#------------------------------------------------------------------------------

class CloseAllAction(Action):
    """ An action for closing all editors.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Close all editors"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "C&lose All"

    # A short description of the action used for tooltip text etc:
    tooltip = "Close All (Shift+Ctrl+W)"

    # Keyboard accelerator:
    accelerator = "Shift+Ctrl+W"

    # Is the action enabled?
    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, **traits):
        """ Returns a new CloseAllAction.
        """
        super(CloseAllAction, self).__init__(**traits)

        if traits.has_key("window"):
            traits["window"].on_trait_change(self.on_editors_change,
                "editors_items")

    #--------------------------------------------------------------------------
    #  "CloseAllAction" interface:
    #--------------------------------------------------------------------------

    def on_editors_change(self, event):
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
        """ Perform the action.
        """
        editors = self.window.editors[:]

        for editor in editors:
            self.window.close_editor(editor)

# EOF -------------------------------------------------------------------------
