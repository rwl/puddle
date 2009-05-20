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

""" Defines wizard for file resource creation """

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists

from enthought.io.api import File

from enthought.traits.api import \
    HasTraits, Directory, Bool, Str, Property, Instance, cached_property, \
    Delegate, Event

from enthought.traits.ui.api import \
    View, Item, Group, Label, Heading, DirectoryEditor

from enthought.traits.ui.menu import OKCancelButtons
from enthought.pyface.api import ImageResource
from enthought.pyface.wizard.api import SimpleWizard, WizardPage

from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.wizard_extension import WizardExtension

from puddle.resource.wizard.container_selection_page import \
    ContainerSelectionPage

from puddle.resource.i_workspace import IWorkspace
from puddle.resource.resource_view import RESOURCE_VIEW

#------------------------------------------------------------------------------
#  "FilePage" class:
#------------------------------------------------------------------------------

class FilePage(WizardPage):
    """ Wizard page for file creation.
    """

    #--------------------------------------------------------------------------
    #  FolderWizardPage interface:
    #--------------------------------------------------------------------------

    # The folder name
    name = Str

    # The containing folder
#    parent = Instance(File)
    csp = Instance(ContainerSelectionPage)

    # Absolute path for the project
    abs_path = Property(Str, depends_on=["name"])

    # A label with advice
    _label = Property(
        Str("Create a new file resource."),
        depends_on=["name"]
    )

    # Has the folder's name been changed
    _named = Bool(False)

    # The default view
    traits_view = View(
        Group(
            Heading("File"),
            Item("_label", style="readonly", show_label=False),
            "_",
        ),
        Item("name")
    )


    def _get_abs_path(self):
        """ Property getter.
        """
        return join(self.csp.directory, self.name)


    def _get__label(self):
        """ Property getter.
        """
        if (exists(self.abs_path)) and (len(self.name) != 0):
            l = "A file with that name already exists."
            self.complete = False
        elif len(self.name) == 0 and self._named:
            l = "File name must be specified"
            self.complete = False
        elif len(self.name) == 0:
            l = "Create a new file resource."
            self.complete = False
        else:
            l = "Create a new file resource."
            self.complete = True

        return l


    def _name_changed(self):
        """ Sets a flag when the name is changed.
        """
        self._named = True

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")
        return ui.control

#------------------------------------------------------------------------------
#  "NewFileWizard" class:
#------------------------------------------------------------------------------

class NewFileWizard(SimpleWizard):
    """ A wizard for file creation.
    """
    # The dialog title
    title = Str("New File")

    #--------------------------------------------------------------------------
    #  "NewFileWizard" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    finished = Event

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, window, **traits):
        """ Returns a NewFileWizard """

        self.window = window

        workspace = window.application.get_service(IWorkspace)

        csp = ContainerSelectionPage(id="container_page", workspace=workspace)
        fwp = FilePage(id="file_page", csp=csp)

        self.pages = [csp, fwp]

        super(NewFileWizard, self).__init__(**traits)

    #--------------------------------------------------------------------------
    #  "NewFileWizard" interface:
    #--------------------------------------------------------------------------

    def _finished_fired(self):
        """ Performs the file resource creation if the wizard is
        finished successfully.

        """

        csp = self.pages[0]
        fwp = self.pages[1]

        file = File(fwp.abs_path)
        file.create_file()

        # Refresh the workspace tree view
        view = self.window.get_view_by_id(RESOURCE_VIEW)
        if view is not None:
            # FIXME: Refresh the parent folder, not the whole tree.
            workspace = self.window.application.get_service(IWorkspace)
            wtv = view.tree_viewer.refresh(workspace)

#------------------------------------------------------------------------------
#  "NewFileWizardExtension" class:
#------------------------------------------------------------------------------

class NewFileWizardExtension(WizardExtension):
    """ Contributes a new file wizard .
    """
    # The wizard contribution's globally unique identifier.
    id = "puddle.python_editor.new_file_wizard"

    # Human readable identifier
    name = "File"

    # The wizards's image (displayed on selection etc)
    image = ImageResource("document")

    # The class of contributed wizard
    wizard_class = "puddle.python_editor.new_file_wizard:" \
        "NewFileWizard"

    # A longer description of the wizard's function
    description = "Create a new file resource"

# EOF -------------------------------------------------------------------------
