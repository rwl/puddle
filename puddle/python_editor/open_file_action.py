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

""" An action for opening a Python script from the file system.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists

from enthought.io.api import File
from enthought.pyface.api import ImageResource, FileDialog, CANCEL
from enthought.pyface.action.api import Action

from puddle.resource.action.open_action import OpenAction

#------------------------------------------------------------------------------
#  "OpenFileAction" class:
#------------------------------------------------------------------------------

class OpenFileAction(Action):
    """ An action for opening a Python script from the file system.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Open a file on the file system"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "Open File&..."

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        dialog = FileDialog(
            parent = self.window.control,
            title="Open File",
            action = "open",
#            default_directory="/tmp",
            wildcard = FileDialog.WILDCARD_PY
        )
        if dialog.open() != CANCEL:
            file = File(dialog.path)
#            self.window.edit(file, PythonWorkbenchEditor)

            self.window.selection = [file]
            OpenAction(window=self.window).perform(event=None)

        return

# EOF -------------------------------------------------------------------------
