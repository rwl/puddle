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

""" Defines a wizard page for resource selection.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists

from enthought.io.file import File

from enthought.traits.api import Instance, Bool
from enthought.pyface.wizard.api import WizardPage

from puddle.resource.i_workspace import IWorkspace
#from puddle.resource.resource import Workspace, File
from puddle.resource.resource_tree_viewer import ResourceTreeViewer

#------------------------------------------------------------------------------
#  "ResourceSelectionPage" class:
#------------------------------------------------------------------------------

class ResourceSelectionPage(WizardPage):
    """ Wizard page for resource selection.
    """

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    complete = Bool(False)

    #--------------------------------------------------------------------------
    #  "ResourceSelectionPage" interface:
    #--------------------------------------------------------------------------

    # The workspace from which the file may be selected
    workspace = Instance(IWorkspace, allow_none=False)

    # The selected parent folder
    resource = Instance(File)

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page. """

        tree_viewer = ResourceTreeViewer(
            parent=parent, input=self.workspace,
            selection_mode="single", show_root=False)

        tree_viewer.on_trait_change(self.on_selection_change, "selection")

        return tree_viewer.control

    #--------------------------------------------------------------------------
    #  "ResourceSelectionPage" interface:
    #--------------------------------------------------------------------------

    def on_selection_change(self, selections):
        """ Handles the tree viewer selections changing.
        """
        if selections:
            selection = selections[0]

            if isinstance(selection, File):
                self.resource = selection
                self.complete = True
            else:
                self.resource = None
                self.complete = False

# EOF -------------------------------------------------------------------------
