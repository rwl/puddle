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

""" Resource plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

import sys

from os import mkdir

from os.path import dirname, isdir, join, exists, basename, expanduser

from enthought.etsconfig.api import ETSConfig
from enthought.envisage.api import Plugin, ExtensionPoint, ServiceOffer
from enthought.traits.api import List, Instance, String, Callable, implements
from enthought.pyface.api import error

from enthought.io.api import File as IOFile

#from workspace_launcher import WorkspaceLauncher

from i_workspace import IWorkspace

#------------------------------------------------------------------------------
#  Logging:
#------------------------------------------------------------------------------

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

EDITORS        = "puddle.resource.editors"
NEW_WIZARDS    = "puddle.resource.new_wizards"
IMPORT_WIZARDS = "puddle.resource.import_wizards"
EXPORT_WIZARDS = "puddle.resource.export_wizards"

#------------------------------------------------------------------------------
#  "File" class:
#------------------------------------------------------------------------------

class File(IOFile):

    implements(IWorkspace)

#------------------------------------------------------------------------------
#  "ResourcePlugin" class:
#------------------------------------------------------------------------------

class ResourcePlugin(Plugin):
    """ Resource plug-in.
    """
    # Extension point IDs.
    SERVICE_OFFERS = "enthought.envisage.service_offers"
    VIEWS = "enthought.envisage.ui.workbench.views"
    PREFERENCES_PAGES = "enthought.envisage.ui.workbench.preferences_pages"
    ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"
    BINDINGS = "enthought.plugins.python_shell.bindings"

    # Unique plugin identifier.
    id = "puddle.resource"

    # Human readable plugin name.
    name = "Resource"

    #--------------------------------------------------------------------------
    #  Extension points:
    #--------------------------------------------------------------------------

    new_wizards = ExtensionPoint(List(Callable), id=NEW_WIZARDS)

    import_wizards = ExtensionPoint(List(Callable), id=IMPORT_WIZARDS)

    export_wizards = ExtensionPoint(List(Callable), id=EXPORT_WIZARDS)

    editors = ExtensionPoint(List(Callable), id=EDITORS)

    #--------------------------------------------------------------------------
    #  Extensions (Contributions):
    #--------------------------------------------------------------------------

    # Contributed services:
    resource_service_offers = List(contributes_to=SERVICE_OFFERS)

    # Contributed views:
    contributed_views = List(contributes_to=VIEWS)

    # Contributed preference pages:
    preferences_pages = List(contributes_to=PREFERENCES_PAGES)

    # Contributed action sets:
    action_sets = List(contributes_to=ACTION_SETS)

    # Contributed bindings:
    bindings_extensions = List(contributes_to=BINDINGS)

    # Contributed new element wizards:
    new_resource_wizards = List(contributes_to=NEW_WIZARDS)

    # Contributed resource import wizards:
    import_resource_wizards = List(contributes_to=IMPORT_WIZARDS)

    # Contributed export wizards:
    export_resource_wizards = List(contributes_to=EXPORT_WIZARDS)

    #--------------------------------------------------------------------------
    #  "Plugin" interface:
    #--------------------------------------------------------------------------

#    def start(self):
#        """ Start the plug-in. """
#
#        prompt = self.application.preferences.get(
#            "enthought.plugins.workspace.prompt", "True"
#        )
#
#        default_path = self.application.preferences.get(
#            "enthought.plugins.workspace.default",
#            join(expanduser("~"), "workspace")
#        )
#
#        # FIXME: Implement preferences helper for type coercion
#        if (prompt == "True") or (not exists(default_path)):
#            # Note that we always offer the service via its name, but look it up
#            # via the actual protocol.
#            from i_workspace import IWorkspace
#
#            workspace = self.application.get_service(IWorkspace)
#            wl = WorkspaceLauncher(
#                workspace=workspace, app_name=self.application.name
#            )
#
#            retval = wl.edit_traits(kind="livemodal")
#            if retval.result:
#                # The preference trait is the opposite to the dialog trait
#                prompt_pref = not wl.default
#                # Set the preferences
#                self.application.preferences.set(
#                    "enthought.plugins.workspace.prompt", prompt_pref
#                )
#                self.application.preferences.set(
#                    "enthought.plugins.workspace.default",
#                    wl.workspace.absolute_path
#                )
#
#                # If a workspace didn't exist we would have to create one
#                if not wl.workspace.exists:
#                    try:
#                        wl.workspace.create_workspace()
#                    except ValueError:
#                        error(
#                            self.window.control, title="Error",
#                            message="An error was encountered trying to "
#                            "create the workspace."
#                        )
#                        self._exit_application()
#                del wl
#            else:
#                self._exit_application()
#
#        # TODO: Implement workspace refresh on start up
#
#        return


    def stop(self):
        """ Stop the plug-in.
        """
        from i_workspace import IWorkspace
        workspace = self.application.get_service(IWorkspace)

        self.application.preferences.set("puddle.resource.default",
            workspace.absolute_path)

    #--------------------------------------------------------------------------
    #  "ResourcePlugin" interface:
    #--------------------------------------------------------------------------

    def _resource_service_offers_default(self):
        """ Trait initialiser.
        """
        resource_service_offer = ServiceOffer(
            protocol="puddle.resource.i_workspace.IWorkspace",
            factory=self._create_workspace_service)

        return [resource_service_offer]


    def _contributed_views_default(self):
        """ Trait initialiser.
        """
        from resource_view import ResourceView
        from resource_tree_view import ResourceTreeView

        return [ResourceView]


    def _preferences_pages_default(self):
        """ Trait initialiser.
        """
        from resource_preferences_page import ResourcePreferencesPage

        return [ResourcePreferencesPage]


    def _action_sets_default(self):
        """ Trait initialiser.
        """
        from resource_action_set import \
            ResourceActionSet, ContextMenuActionSet

        return [ResourceActionSet, ContextMenuActionSet]


    def _bindings_extensions_default(self):
        """ Trait initialiser.
        """
        from i_workspace import IWorkspace
        workspace = self.application.get_service(IWorkspace)

        return [{"workspace": workspace}]


    def _new_resource_wizards_default(self):
        """ Trait initialiser.
        """
        from resource_wizard_extension import FolderWizardExtension

        return [FolderWizardExtension]


    def _import_resource_wizards_default(self):
        """ Trait initialiser.
        """
        from resource_wizard_extension import ImportFileSystemWizardExtension

        return []


    def _export_resource_wizards_default(self):
        """ Trait initialiser.
        """
        return []

    #--------------------------------------------------------------------------
    #  Private interface:
    #--------------------------------------------------------------------------

    def _create_workspace_service(self):
        """ Factory method for the "Workspace" service.
        """
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs an "IWorkspace" service.
#        from resource import File

        path = self.application.preferences.get("puddle.resource.default",
            expanduser("~"))

        return File(path)


#    def _exit_application(self):
#        """ Stops all plug-ins and exits.
#        """
#        # FIXME: Is there a cleaner way of exiting?
#        self.application.stop()
#        sys.exit()

# EOF -------------------------------------------------------------------------
