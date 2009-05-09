#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Envisage IDE plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import List

from enthought.envisage.api import Plugin

#------------------------------------------------------------------------------
#  "EnvisagePlugin" class:
#------------------------------------------------------------------------------

class EnvisagePlugin(Plugin):
    """ Overridden actions and preferences pages.
    """

    #--------------------------------------------------------------------------
    #  "Plugin" interface:
    #--------------------------------------------------------------------------

    # Unique plugin identifier.
    id = "envisage.envisage_plugin"

    # Human readable plugin name.
    name = "Envisage"

    #--------------------------------------------------------------------------
    #  "EnvisagePlugin" interface:
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
        from welcome_action import EnvisageActionSet

        return [EnvisageActionSet]

# EOF -------------------------------------------------------------------------
