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

""" Defines an action for running a Python file.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.io.api import File
from enthought.traits.api import Instance
from enthought.traits.ui.menu import Action
from enthought.pyface.api import ImageResource
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

#------------------------------------------------------------------------------
#  "RunAsPythonAction" class:
#------------------------------------------------------------------------------

class PythonRunAction(Action):
    """ Action for running a Python file.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Run the file in the Python shell"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Python Run"

    # A short description of the action used for tooltip text etc:
    tooltip = "Python Run"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("python")

    # Keyboard accelerator:
    accelerator = "Ctrl+R"

    #--------------------------------------------------------------------------
    #  "PythonRunAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "PythonRunAction" interface:
    #--------------------------------------------------------------------------

    def _selection_changed_for_window(self, new):
        """ Enables the action when a File object is selected.
        """
        if len(new) == 1:
            selection = new[0]
            if isinstance(selection, File) and (selection.ext == ".py"):
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
            if isinstance(sel, File) and (sel.ext == ".py"):
                return True
            else:
                return False
        else:
            return False


    def perform(self, event):
        """ Perform the action.
        """
        selected = self.window.selection[0]

        # The file must be saved first!
#        self.save()

        # Execute the code.
        if len(selected.path) > 0:
            view = self.window.get_view_by_id(
                'enthought.plugins.python_shell_view')

            if view is not None:
                view.execute_command('execfile(r"%s")' % selected.path,
                    hidden=False)

        return

# EOF -------------------------------------------------------------------------
