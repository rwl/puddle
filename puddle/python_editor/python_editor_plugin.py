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

""" Python editor plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.plugins.text_editor.text_editor_plugin import TextEditorPlugin

from enthought.traits.api import List, Dict, String

#------------------------------------------------------------------------------
#  "PythonEditorPlugin" class:
#------------------------------------------------------------------------------

class PythonEditorPlugin(TextEditorPlugin):
    """ Python editor plug-in.
    """

    # Extension point IDs
    ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"
    NEW_WIZARDS = "puddle.resource.new_wizards"
    EDITORS = "puddle.resource.editors"

    # Unique plugin identifier
    id = "puddle.python_editor"

    # Human readable plugin name
    name = "Python Editor"

    #--------------------------------------------------------------------------
    #  Extensions (Contributions):
    #--------------------------------------------------------------------------

    # Contributed new resource wizards:
    new_wizards = List(contributes_to=NEW_WIZARDS)

    # Contributed workspace editors:
    editors = List(contributes_to=EDITORS)

    #--------------------------------------------------------------------------
    #  "PythonEditorPlugin" interface:
    #--------------------------------------------------------------------------

    def _action_sets_default(self):
        """ Trait initialiser.
        """
        from python_editor_action_set import PythonEditorActionSet

        return [PythonEditorActionSet]


    def _new_wizards_default(self):
        """ Trait initialiser.
        """
        from new_file_wizard import NewFileWizardExtension

        return [NewFileWizardExtension]


    def _editors_default(self):
        """ Trait initialiser.
        """
        from python_editor_extension import \
            PythonEditorExtension, TextEditorExtension

        return [PythonEditorExtension, TextEditorExtension]

# EOF -------------------------------------------------------------------------
