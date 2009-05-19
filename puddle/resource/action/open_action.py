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

""" Workspace plug-in actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.io.api import File
from enthought.traits.api import Bool, Instance
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.resource_editor import ResourceEditor

from puddle.resource.resource_plugin import EDITORS

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "OpenAction" class:
#------------------------------------------------------------------------------

class OpenAction(Action):
    """ Defines an action that open the current resource.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Open the active resource"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Open"

    # A short description of the action used for tooltip text etc:
    tooltip = "Open"

    # Is the action enabled?
    enabled = Bool(True)

    # Is the action visible?
    visible = Bool(False)

    #--------------------------------------------------------------------------
    #  "CloseAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "OpenAction" interface:
    #--------------------------------------------------------------------------

    def _selection_changed_for_window(self, selections):
        """ Makes the action visible if a File is selected.
        """
        if selections:
            selection = selections[0]
            # Enable the action if a valid editor has been contributed
            editors = self.window.application.get_extensions(EDITORS)
            exts = [ext for factory in editors for ext in factory().extensions]
            if isinstance(selection, File) and (selection.ext in exts):
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
        sel = self.window.selection

        editors = self.window.application.get_extensions(EDITORS)
        exts = [ext for factory in editors for ext in factory().extensions]

        if sel and isinstance(sel[0], File) and (sel[0].ext in exts):
            return True
        else:
            return False


    def _visible_default(self):
        """ Trait initialiser.
        """
        sel = self.window.selection

        editors = self.window.application.get_extensions(EDITORS)
        exts = [ext for factory in editors for ext in factory().extensions]

        if sel and isinstance(sel[0], File) and (sel[0].ext in exts):
            return True
        else:
            return False


    def perform(self, event):
        """ Performs the action.
        """
        app = self.window.application
        editors = [factory() for factory in app.get_extensions(EDITORS)]

        selections = self.window.selection
        if selections:
            # Use the first of the selected objects
            selection = selections[0]

            if isinstance(selection, File):
                valid_editors = [
                    e for e in editors if selection.ext in e.extensions]

                if valid_editors:
                    for editor in valid_editors:
                        if editor.default:
                            break
                    else:
                        editor = valid_editors[0]
                    default_editor = app.import_symbol(editor.editor_class)
                    self.window.edit(selection, default_editor)
                else:
                    # FIXME: Show info dialog?
                    pass

# EOF -------------------------------------------------------------------------
