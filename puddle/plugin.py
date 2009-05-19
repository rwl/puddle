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

""" Puddle IDE plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import List
from enthought.envisage.api import Plugin

#------------------------------------------------------------------------------
#  "PuddlePlugin" class:
#------------------------------------------------------------------------------

class PuddlePlugin(Plugin):
    """ Overridden actions and preferences pages.
    """

    #--------------------------------------------------------------------------
    #  "Plugin" interface:
    #--------------------------------------------------------------------------

    # Unique plugin identifier.
    id = "puddle.puddle_plugin"

    # Human readable plugin name.
    name = "Puddle"

    #--------------------------------------------------------------------------
    #  "PuddlePlugin" interface:
    #--------------------------------------------------------------------------

    # The Ids of the extension points that this plugin offers.
    VIEWS = "enthought.envisage.ui.workbench.views"
    PERSPECTIVES = "enthought.envisage.ui.workbench.perspectives"
    ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"

    # Contributions to the views extension point made by this plug-in.
    my_views = List(contributes_to=VIEWS)

    # Contributions to the perspective extension point made by this plug-in.
    my_perspectives = List(contributes_to=PERSPECTIVES)

    # Contributions to the action set extension point made by this plug-in.
    my_action_sets = List(contributes_to=ACTION_SETS)

    #--------------------------------------------------------------------------
    #  Private interface:
    #--------------------------------------------------------------------------

    def _my_views_default(self):
        """ Trait initialiser.
        """
        from welcome_view import WelcomeView

        return [WelcomeView]


    def _my_perspectives_default(self):
        """ Trait initialiser.
        """
        from perspective import WelcomePerspective, DefaultPerspective

        return [WelcomePerspective, DefaultPerspective]


    def _my_action_sets_default(self):
        """ Trait initialiser.
        """
        from welcome_action import PuddleActionSet

        return [PuddleActionSet]

# EOF -------------------------------------------------------------------------
