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

""" Defines classes for use as dialog boxes with the workspace plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists

from enthought.io.api import File

from enthought.traits.api import \
    HasTraits, Directory, Bool, Str, Property, Instance, cached_property

from enthought.pyface.wizard.api import SimpleWizard, WizardPage

from enthought.plugins.workspace.workspace_tree_viewer import \
    WorkspaceTreeViewer, AllowOnlyFolders

#------------------------------------------------------------------------------
#  "FolderSelectionWizardPage" class:
#------------------------------------------------------------------------------

class FolderSelectionWizardPage(WizardPage):
    """ Wizard page for parent folder selection.
    """
    # The workspace from which the folder may be selected
    workspace = Instance(File, allow_none=False)

    # The selected parent folder
    folder = Instance(File)

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page.
        """
        tree_viewer = WorkspaceTreeViewer(
            parent=parent, input=self.workspace,
#            filters=[AllowOnlyFolders()],
            show_root=False)

        tree_viewer.on_trait_change(self.on_selection_change, "selection")

        return tree_viewer.control


    def on_selection_change(self, selection):
        """ Relates the folder selected in the tree viewer to the wizard
            page's folder trait.
        """
        if selection:
            self.folder = selection[0]


    def _folder_changed(self, new):
        """ Complete the wizard when an existing folder is set.
        """
        if (new is not None) and new.exists:
            self.complete = True
        else:
            self.complete = False

# EOF -------------------------------------------------------------------------
