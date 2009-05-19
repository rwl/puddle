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

""" Extended Workbench plug-in actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Instance, on_trait_change
from enthought.pyface.api import ImageResource, OK
from enthought.pyface.action.api import Action
from enthought.pyface.wizard.api import ChainedWizard

from puddle.resource.wizard.wizard_selection_wizard \
    import WizardSelectionWizard

from puddle.resource.resource_plugin import NEW_WIZARDS

from common import IMAGE_LOCATION

#------------------------------------------------------------------------------
#  "NewResourceAction" class:
#------------------------------------------------------------------------------

class NewResourceAction(Action):
    """ Defines an action that opens the new resource creation wizard.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action:
    description = "Create a new resource"

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "&Other..."

    # A short description of the action used for tooltip text etc:
    tooltip = "New"

    # The action's image (displayed on tool bar tools etc):
    image = ImageResource("new", search_path=[IMAGE_LOCATION])

    # Keyboard accelerator
    accelerator = "Ctrl+N"

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Performs the action.
        """
        # Get all contributed new resource wizards
        contrib = self.window.application.get_extensions(NEW_WIZARDS)
        # Instantiate the contributed classes
        wizards = [wizard() for wizard in contrib]

        # Create the wizard...
        wizard = WizardSelectionWizard(parent=self.window.control,
            window=self.window, wizards=wizards, title="New")

        # ...open the wizard.
        if wizard.open() == OK:
            wizard.next_wizard.finished = True

        return

# EOF -------------------------------------------------------------------------
