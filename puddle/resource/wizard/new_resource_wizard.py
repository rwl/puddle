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

""" Defines a wizard for new resource creation.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists, splitext

from enthought.io.api import File as IOFile

from enthought.traits.api import \
    HasTraits, Directory, Bool, List, Str, Float, Property, Instance, \
    cached_property, Event

from enthought.traits.ui.api import \
    View, Item, Group, Label, Heading, DirectoryEditor

from enthought.pyface.wizard.api import SimpleWizard, WizardPage
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.i_workspace import IWorkspace
from puddle.resource.action.open_action import OpenAction
#from puddle.resource.resource_adapter import PickleFileIResourceAdapter
from puddle.resource.resource_view import RESOURCE_VIEW

from container_selection_page import ContainerSelectionPage

#------------------------------------------------------------------------------
#  "NewResourceWizardPage" class:
#------------------------------------------------------------------------------

class NewResourceWizardPage(WizardPage):
    """ Wizard page for new resource creation.
    """
    # Valid file extensions for the resource.
    extensions = List(Str, [".pkl"])

    # Name for the new file resource..
    resource_name = Str

    # Wizard page for container selection.
    csp = Instance(ContainerSelectionPage)

    # Absolute path for the resource.
    abs_path = Property(Str, depends_on=["resource_name"])

    # A label with advice.
    _label = Property( Str("Create a new resource."),
        depends_on=["resource_name"] )

    # Has the network's name been changed?
    _named = Bool(False)

    # The default view
    traits_view = View(
        Group(Heading("Resource"),
              Item("_label", style="readonly", show_label=False),
              "_"),
        Item("resource_name") )


    @cached_property
    def _get_abs_path(self):
        """ Property getter.
        """
        return join(self.csp.directory, self.resource_name)


    @cached_property
    def _get__label(self):
        """ Property getter
        """
        name = self.resource_name

        if (exists(self.abs_path)) and (len(name) != 0):
            l = "A resource with that name already exists."
            self.complete = False
        elif len(name) == 0 and self._named:
            l = "Resource name must be specified."
            self.complete = False
        elif not name.endswith( tuple(self.extensions) ):
            l = "The resource file extension must be in %s." % \
                self.extensions
            self.complete = False
        elif len(name) == 0:
            l = "Create a new resource."
            self.complete = False
        else:
            l = "Create a new resource."
            self.complete = True

        return l


    def _resource_name_changed(self):
        """ Sets a flag when the name is changed.
        """
        self._named = True

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Creates the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")

        return ui.control

#------------------------------------------------------------------------------
#  "NewResourceWizard" class:
#------------------------------------------------------------------------------

class NewResourceWizard(SimpleWizard):
    """ A wizard for new resource creation.
    """
    # Valid file extensions for the resource.
    extensions = List(Str, [".pkl"])

    # The dialog title
    title = Str("New Resource")

    #--------------------------------------------------------------------------
    #  "NetworkWizard" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    finished = Event

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, window, **traits):
        """ Initialises the wizard.
        """
        self.window = window
        workspace = window.application.get_service(IWorkspace)

        csp = ContainerSelectionPage(id="container_page", workspace=workspace)
        nwp = NewResourceWizardPage(id="resource_page",
            extensions=self.extensions, csp=csp)

        self.pages = [csp, nwp]

        super(NewResourceWizard, self).__init__(**traits)


    def get_resource(self, file):
        """ Returns the new adapted resource. Override in subclasses.
        """
#        return PickleFileIResourceAdapter(file)
        raise NotImplementedError


    def get_content(self, name):
        """ Returns the content for the new resource. Override in subclasses.
        """
        return None

    #--------------------------------------------------------------------------
    #  "NewResourceWizard" interface:
    #--------------------------------------------------------------------------

    def _finished_fired(self):
        """ Performs the resource creation if the wizard is
            finished successfully.
        """
        workspace = self.window.application.get_service(IWorkspace)

        csp = self.pages[0]
        nrwp = self.pages[1]

        file = IOFile(join(csp.directory, nrwp.resource_name))

        if not file.exists:
            name, ext = splitext( nrwp.resource_name )

            content = self.get_content(name)
            resource = self.get_resource(file)

            resource.save( content )

        self._open_resource(file)

        self._refresh_container(workspace)


    def _open_resource(self, file):
        """ Makes the file the current selection and opens it.
        """
        self.window.selection = [file]
        OpenAction(window=self.window).perform(event=None)


    def _refresh_container(self, container):
        """ Refreshes the workspace tree view.
        """
        view = self.window.get_view_by_id(RESOURCE_VIEW)
        if view is not None:
            view.tree_viewer.refresh(container)

# EOF -------------------------------------------------------------------------
