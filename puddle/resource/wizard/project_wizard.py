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

""" Defines a wizard for project creation.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists, join

from enthought.traits.api import \
    Str, Directory, Property, Bool, Instance, Event, \
    cached_property, on_trait_change

from enthought.traits.ui.api import View, Group, Item, Heading

from enthought.pyface.wizard.api import \
    SimpleWizard, WizardPage, SimpleWizardController

from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from puddle.resource.i_workspace import IWorkspace
from puddle.resource.resource_view import RESOURCE_VIEW

#------------------------------------------------------------------------------
#  "ProjectWizardPage" class:
#------------------------------------------------------------------------------

class ProjectWizardPage(WizardPage):
    """ Wizard page for project creation.
    """

    #--------------------------------------------------------------------------
    #  ProjectWizardPage interface:
    #--------------------------------------------------------------------------

    # The project name
    project_name = Str

    # The location for the new project
    location = Directory(auto_set=True)

    # Absolute path for the project
    abs_path = Property(Str, depends_on=["project_name", "location"])

    # Should we use the default (workspace) location?
    use_default = Bool(True)

    # A label with advice
    _label = Property(Str("Create a new project resource."),
        depends_on=["project_name", "location"])

    # Has the project name been changed
    _named = Bool(False)

    # The default view:
    traits_view = View(
        Group(Heading("Project")),
        Group(
            Item(name="_label", style="readonly", show_label=False),
            "_",
        ),
        Group(Item(name="project_name")),
        Group(
            Item(name="use_default", label="Use default location"),
            show_left=False
        ),
        Item(name="location", enabled_when="use_default==False")
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
    def _get_abs_path(self):
        """ Property getter.
        """
        return join(self.location, self.project_name)


    @cached_property
    def _get__label(self):
        """ Property getter.
        """
        if (exists(self.abs_path)) and (len(self.project_name) != 0):
            l = "A project with that name already exists."
            self.complete = False
        elif len(self.project_name) == 0 and self._named:
            l = "Project name must be specified"
            self.complete = False
        elif not exists(self.location):
            l = "Project location directory does not exist"
            self.complete = False
        elif len(self.location) == 0:
            l = "Project location directory must be specified"
            self.complete = False
        elif len(self.project_name) == 0:
            l = "Create a new project resource."
            self.complete = False
        else:
            l = "Create a new project resource."
            self.complete = True

        return l


    def _project_name_changed(self):
        """ Sets a flag when the name is changed.
        """
        self._named = True

#------------------------------------------------------------------------------
#  "ProjectWizard" class:
#------------------------------------------------------------------------------

class ProjectWizard(SimpleWizard):
    """ A wizard for project creation.
    """

    # The dialog title
    title = Str("New Project")

#    controller = Instance(ProjectWizardController)

    #--------------------------------------------------------------------------
    #  "ProjectWizard" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    finished = Event

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, window, **traits):
        """ Returns a ProjectWizard.
        """
        self.window = window

        workspace = window.application.get_service(IWorkspace)

        self.pages = [
            ProjectWizardPage(
                id="project_page", location=workspace.absolute_path
            )
        ]

        super(ProjectWizard, self).__init__(**traits)


    def _finished_fired(self):
        """ Performs the project resource creation if the wizard is
            finished successfully.
        """
#        try:
        workspace = self.window.application.get_service(IWorkspace)

        pwp = self.pages[0]
        project = workspace.get_project(pwp.project_name)
        if not project.exists:
            project.create_project()

#        except ValueError:
#            error(
#                self.window.control, title="Error",
#                message="An error was encountered trying to "
#                "create the project."
#            )

        # Refresh the workspace tree view
        view = self.window.get_view_by_id(RESOURCE_VIEW)
        if view is not None:
            wtv = view.tree_viewer.refresh(workspace)


#    def _controller_default(self):
#        """ Provide a default controller. """
#
#        return ProjectWizardController()

#------------------------------------------------------------------------------
#  Standalone call:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    from enthought.pyface.api import GUI

    # Create the GUI.
    gui = GUI()

    wizard = ProjectWizard(parent=None)

    # Open the wizard
    wizard.open()

    # Start the GUI event loop!
    gui.start_event_loop()

# EOF -------------------------------------------------------------------------
