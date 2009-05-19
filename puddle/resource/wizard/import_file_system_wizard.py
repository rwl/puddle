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

""" Defines a wizard for importing resources from the file system to
    an existing project.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists, join

from enthought.traits.api import \
    Str, Directory, Property, Bool, cached_property

from enthought.traits.ui.api import View, Group, Item, Heading

from enthought.pyface.wizard.api import SimpleWizard, WizardPage

from puddle.resource.resource_dialog import FolderSelectionWizardPage

#------------------------------------------------------------------------------
#  "ImportFileSystemWizardPage" class:
#------------------------------------------------------------------------------

class ImportFileSystemWizardPage(WizardPage):
    """ Wizard page for selection of files for import.
    """

    #--------------------------------------------------------------------------
    #  ImportFileSystemWizardPage interface:
    #--------------------------------------------------------------------------

    # The file system directory from which to import
    from_directory = Directory(auto_set=True)

    # A label with instructions
    _label = Property(Str, depends_on=["from_directory"])

    # The default view:
    traits_view = View(
        Group(Heading("File system")),
        Group(
            Item(name="_label", style="readonly", show_label=False),
            "_",
        ),
        Item(name="from_directory")
    )

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind='subpanel')

        return ui.control

    #--------------------------------------------------------------------------
    #  Private interface.
    #--------------------------------------------------------------------------

    @cached_property
    def _get__label(self):
        """ Property getter.
        """
        l = "Import resources from the local file system into " \
            "an existing project."
        self.complete = True

        return l

#------------------------------------------------------------------------------
#  "ProjectWizard" class:
#------------------------------------------------------------------------------

class ImportFileSystemWizard(SimpleWizard):
    """ A wizard for importing resources from the file system
        to an existing project.
    """

    # The dialog title
    title = "Import"

    def __init__(self, workspace, **traits):
        """ Returns a ProjectWizard.
        """
        self.pages = [
            FolderSelectionWizardPage(
                id="folder_selection", workspace=workspace
            ),
            ImportFileSystemWizardPage(id="file_system", from_directory="/tmp")
        ]

        super(ImportFileSystemWizard, self).__init__(**traits)

#------------------------------------------------------------------------------
#  Standalone call:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    from enthought.pyface.api import GUI

    # Create the GUI.
    gui = GUI()

    wizard = ImportFileSystemWizard(parent=None, workspace="/tmp")

    # Open the wizard
    wizard.open()

    # Start the GUI event loop!
    gui.start_event_loop()

# EOF -------------------------------------------------------------------------
