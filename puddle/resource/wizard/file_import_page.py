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

""" Defines a generic wizard page for file import.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists

from enthought.traits.api import File, Property, Str, cached_property
from enthought.traits.ui.api import View, Group, Item, Heading
from enthought.pyface.wizard.api import WizardPage

#------------------------------------------------------------------------------
#  "FileImportPage" class:
#------------------------------------------------------------------------------

class FileImportPage(WizardPage):
    """ Defines a wizard page for file selection.
    """
    # The name of the file type
    file_type = Str

    data_file = File(exists=True, filter=["All Files|*.*"])

    # A label with instructions
    _label = Property(Str, depends_on=["data_file"])

    traits_view = View(
        Group(Heading("File"),
            Item("_label", style="readonly", show_label=False),
            "_"),
        Item("data_file") )

    #--------------------------------------------------------------------------
    #  "FileImportPage" interface:
    #--------------------------------------------------------------------------

    @cached_property
    def _get__label(self):
        """ Property getter.
        """
        if not exists(self.data_file):
            l = "Select a %s file." % self.file_type
            self.complete = False
        else:
            l = "Click Finish to continue."
            self.complete = True

        return l

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Create the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")

        return ui.control

# EOF -------------------------------------------------------------------------
