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

""" Resource wizard extensions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.pyface.api import ImageResource

from wizard_extension import WizardExtension

#------------------------------------------------------------------------------
#  "FolderWizard" class:
#------------------------------------------------------------------------------

class FolderWizardExtension(WizardExtension):
    """ Contributes a new folder wizard.
    """

    # The wizard contribution's globally unique identifier.
    id = "puddle.resource.folder_wizard"

    # Human readable identifier
    name = "Folder"

    # The wizards's image (displayed on selection etc)
    image = ImageResource("new")

    # The class of contributed wizard
    wizard_class = "puddle.resource.wizard.folder_wizard:" \
        "FolderWizard"

    # A longer description of the wizard's function
    description = "Create a new folder resource"

#------------------------------------------------------------------------------
#  "ImportFileSystemWizard" class:
#------------------------------------------------------------------------------

class ImportFileSystemWizardExtension(WizardExtension):
    """ Contributes a wizard for importing resources from the file system
        to existing projects.
    """

    # The wizard contribution's globally unique identifier.
    id = "puddle.resource.file_system_import_wizard"

    # Human readable identifier
    name = "File System"

    # The wizards's image (displayed on selection etc)
    image = ImageResource("closed_folder")

    # The class of contributed wizard
    wizard_class = "puddle.resource.wizard." \
        "import_file_system_wizard:ImportFileSystemWizard"

    # A longer description of the wizard's function
    description = "Import resources from the file system to existing projects."

# EOF -------------------------------------------------------------------------
