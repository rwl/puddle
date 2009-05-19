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

""" Defines a wizard page for container selection.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists

from enthought.io.api import File

from enthought.traits.api import \
    HasTraits, Directory, Bool, Str, Property, Instance, cached_property

from enthought.traits.ui.api import View, Item, Group, Heading, Label

from enthought.pyface.wizard.api import SimpleWizard, WizardPage

#------------------------------------------------------------------------------
#  "ContainerSelectionPage" class:
#------------------------------------------------------------------------------

class ContainerSelectionPage(WizardPage):
    """ Wizard page for container selection.
    """

    #--------------------------------------------------------------------------
    #  "ContainerSelectionPage" interface:
    #--------------------------------------------------------------------------

    # The workspace from which the folder may be selected
    workspace = Instance(File)

    # The containing directory
    directory = Directory(exists=True)

    # The default view
    traits_view = View(
        Heading("Container"),
        Label("Enter or select the parent directory"),
#        Item(name="directory", style="text", show_label=False),
        Item(name="directory", style="simple", show_label=False) )

    #--------------------------------------------------------------------------
    #  "ContainerSelectionPage" interface:
    #--------------------------------------------------------------------------

    def _directory_default(self):
        """ Trait initialiser.
        """
        # FIXME: Under Windows if a 'custom' directory editor is used in the
        # view then this initialiser is called after the page has been
        # destroyed and any call to self raises an error.
        if self.workspace is not None:
            self.complete = True
            return self.workspace.absolute_path
        else:
            self.complete = True
            return expanduser("~")


    def _directory_changed(self, new):
        """ Complete the wizard when a container is selected.
        """
        if new != "":
            self.complete = True
        else:
            self.complete = False

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")

        return ui.control

# EOF -------------------------------------------------------------------------
