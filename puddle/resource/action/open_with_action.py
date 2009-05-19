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

""" Resource plug-in actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.io.api import File
from enthought.traits.api import Bool, Str, List, Delegate, Instance
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.editor import Editor

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "OpenWithAction" class:
#------------------------------------------------------------------------------

class OpenWithAction(Action):
    """ Defines an action that opens the current resource.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # The action"s name (displayed on menus/tool bar tools etc):
    name = Delegate("editor")

    # The action's image (displayed on tool bar tools etc):
    image = Delegate("editor")

    # Is the action enabled?
    enabled = Bool(True)

    # Is the action visible?
    visible = Bool(True)

    #--------------------------------------------------------------------------
    #  "OpenWithAction" interface:
    #--------------------------------------------------------------------------

    # The workbench window that the menu is part of.
    window = Instance(WorkbenchWindow)

    # The editor extension
    editor = Instance(Editor)

    #--------------------------------------------------------------------------
    #  "OpenWithAction" interface:
    #--------------------------------------------------------------------------

    def _selection_changed_for_window(self, new):
        """ Makes the action visible if a File with a valid extension
            is selected
        """
        if len(new) == 1:
            sel = new[0]

            if isinstance(sel, File) and (sel.ext in self.editor.extensions):
                    self.enabled = True
            else:
                self.enabled = False
        else:
            self.enabled = False

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def _enabled_default(self):
        """ Trait initialiser.
        """
        if self.window.selection:
            sel = self.window.selection[0]

            if isinstance(sel, File) and (sel.ext in self.editor.extensions):
                return True
            else:
                return False
        else:
            return False


    def perform(self, event):
        """ Performs the action.
        """
        selections = self.window.selection
        if selections:
            # Use the first of the selected objects
            selection = selections[0]

            app = self.window.application
            editor = app.import_symbol(self.editor.editor_class)
            self.window.edit(selection, editor)

# EOF -------------------------------------------------------------------------
