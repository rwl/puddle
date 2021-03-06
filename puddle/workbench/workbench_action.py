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

""" Custom workbench actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import join, dirname

from enthought.traits.api import Instance, Bool
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action

from enthought.envisage.ui.workbench.action.api import \
    ExitAction, EditPreferencesAction, AboutAction

from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

#------------------------------------------------------------------------------
#  "NewWindowAction" class:
#------------------------------------------------------------------------------

class NewWindowAction(Action):
    """ An action that opens a new workbench window.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action.
    description = "Open a new workbench window"

    # The action"s image (displayed on tool bar tools etc).
#    image = ImageResource("window")

    # The action"s name (displayed on menus/tool bar tools etc).
    name = "&New Window"

    # A short description of the action used for tooltip text etc.
    tooltip = "New workbench window"

    #--------------------------------------------------------------------------
    #  "NewWindowAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        window = self.window.workbench.create_window(
            position=self.window.application.window_position,
            size=self.window.application.window_size
        )
        window.open()

#------------------------------------------------------------------------------
#  "NewEditorAction" class:
#------------------------------------------------------------------------------

class NewEditorAction(Action):
    """ An action that opens a new workbench window.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action.
    description = "Open a new editor"

    # The action"s image (displayed on tool bar tools etc).
#    image = ImageResource("window", search_path=[IMAGE_PATH])

    # The action"s name (displayed on menus/tool bar tools etc).
    name = "New &Editor"

    # A short description of the action used for tooltip text etc.
    tooltip = "New editor"

    # Is the action enabled?
    enabled = Bool(False)

    #--------------------------------------------------------------------------
    #  "NewEditorAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action """

        editor = self.window.active_editor

        if editor is not None:
            self.window.edit(editor.obj, type(editor), use_existing=False)

    #--------------------------------------------------------------------------
    #  "NewEditorAction" interface:
    #--------------------------------------------------------------------------

    def _active_editor_changed_for_window(self, new):
        """ Enables the action if the window has one or more open editors """

        if new is not None:
            self.enabled = True
        else:
            self.enabled = False

#------------------------------------------------------------------------------
#  "ExitAction" class:
#------------------------------------------------------------------------------

class ExitAction(ExitAction):
    """ An action that exits the workbench.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action.
    description = "Exit the application"

    # The action"s image (displayed on tool bar tools etc).
    image = ImageResource("exit")

    # The action"s name (displayed on menus/tool bar tools etc).
    name = "E&xit"

    # A short description of the action used for tooltip text etc.
    tooltip = "Exit"

    # Keyboard accelerator:
    accelerator = "Alt+X"

#------------------------------------------------------------------------------
#  "PreferencesAction" class:
#------------------------------------------------------------------------------

class PreferencesAction(EditPreferencesAction):
    """ An action that displays the preferences dialog.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # The action"s image (displayed on tool bar tools etc).
    image = ImageResource("preferences")

#------------------------------------------------------------------------------
#  "AboutAction" class:
#------------------------------------------------------------------------------

class AboutAction(AboutAction):
    """ An action that shows the "About" dialog.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action.
    description = "Display information about the application"

    # The action"s image (displayed on tool bar tools etc).
    image = ImageResource("about")

    # A short description of the action used for tooltip text etc.
    tooltip = "Display information about the application"

#------------------------------------------------------------------------------
#  "UndoAction" class:
#------------------------------------------------------------------------------

class UndoAction(Action):
    """ An action that undoes the active editors last action.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Undo last edit"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Undo"

    # A short description of the action used for tooltip text etc:
    tooltip = "Undo (Ctrl+Z)"

    # Keyboard accelerator:
    accelerator = "Ctrl+Z"

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        editor = self.window.active_editor

        editor.ui.history.undo()

# EOF -------------------------------------------------------------------------
