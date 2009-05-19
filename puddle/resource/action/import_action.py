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

""" Imprort resource action.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.pyface.api import ImageResource, OK
from enthought.pyface.action.api import Action

from envisage.resource.wizard.wizard_selection_wizard \
    import WizardSelectionWizard

from puddle.resource.resource_plugin import IMPORT_WIZARDS

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "ImportAction" class:
#------------------------------------------------------------------------------

class ImportAction(Action):
    """ Defines an action that opens the import wizard selection wizard.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Import resources to the workspace"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Import..."

    # A short description of the action used for tooltip text etc:
    tooltip = "Import resources"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("import", search_path=[IMAGE_LOCATION])

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action.
        """
        # Get all contributed import wizards
        contrib = self.window.application.get_extensions(IMPORT_WIZARDS)
        # Instantiate the contributed classes
        wizards = [wizard() for wizard in contrib]

        # Create the wizard...
        wizard = WizardSelectionWizard( parent=self.window.control,
            window=self.window, wizards=wizards, title="Import" )

        # ...open the wizard.
        if wizard.open() == OK:
            wizard.next_wizard.finished = True

        return

#        # Get all contributed new element wizards
#        app = self.window.workbench.application
#        contrib = app.get_extensions(IMPORT_WIZARDS)
#
#        # Ensure they are not instantiated
#        wizards = []
#        for factory_or_wizard in contrib:
#            if not isinstance(factory_or_wizard, WizardContribution):
#                wizard = factory_or_wizard()
#            else:
#                logger.warn(
#                    "DEPRECATED: contribute wizard classes or "
#                    "factories - not wizard instances."
#                )
#
#                wizard = factory_or_wizard
#            wizards.append(wizard)
#
#        # Create the selection page...
#        wswp = WizardSelectionPage(
#            wizards=wizards, id="wizard_selection"
#        )
#        wswp.on_trait_change(self.on_wizard_changed, "wizard")
#
#        # ...add it to the a wizard...
#        self.wizard = wizard = ChainedWizard(
#            parent=self.window.control, title="New",
#            pages=[wswp]
#        )
#
#        # ...open the wizard.
#        wizard.open()
#
#        return


#    def on_wizard_changed(self, new):
#
#        if new is not None:
#            app = self.window.application
#            wizard_klass = app.import_symbol(new.wizard_class)
#
#            workspace = self.window.application.get_service(WORKSPACE_SERVICE)
#
#            self.wizard.next_wizard = wizard_klass(
#                parent=None, workspace=workspace
#            )

# EOF -------------------------------------------------------------------------
