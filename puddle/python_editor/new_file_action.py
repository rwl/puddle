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

""" Defines an action for creating a new Python script.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists

from enthought.io.api import File
from enthought.pyface.api import ImageResource, FileDialog, CANCEL
from enthought.pyface.action.api import Action

from puddle.resource.action.open_action import OpenAction

from enthought.plugins.text_editor.editor.text_editor import TextEditor

#------------------------------------------------------------------------------
#  "NewFileAction" class:
#------------------------------------------------------------------------------

class NewFileAction(Action):
    """ An action for creating a new Python script.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Create a new file"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "File"

    # A short description of the action used for tooltip text etc:
    tooltip = "Create a File"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("new")

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        file = File("")
        self.window.edit(file, TextEditor)

#        self.window.selection = [file]
#        OpenAction(window=self.window).perform(event=None)

        return

# EOF -------------------------------------------------------------------------
