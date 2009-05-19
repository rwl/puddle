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

""" Workbench plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import List

from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin \
    as EnthoughtWorkbenchPlugin

#------------------------------------------------------------------------------
#  "WorkbenchPlugin" class:
#------------------------------------------------------------------------------

class WorkbenchPlugin(EnthoughtWorkbenchPlugin):
    """ Overridden actions and preferences pages.
    """

    #--------------------------------------------------------------------------
    #  "EnthoughtWorkbenchPlugin" interface:
    #--------------------------------------------------------------------------

    def _my_preferences_pages_default(self):
        """ Trait initialiser.
        """

        from workbench_preferences_page import \
            WorkbenchPreferencesPage

        return [WorkbenchPreferencesPage]


    def _my_action_sets_default(self):
        """ Trait initialiser.
        """
        from workbench_action_set import WorkbenchActionSet

        return [WorkbenchActionSet]

# EOF -------------------------------------------------------------------------
