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

""" Defines an action for displaying the welcome perspective.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import join, dirname

from enthought.traits.api import Instance, Bool, Str
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action as PyFaceAction
from enthought.envisage.ui.action.api import Action, ActionSet, Group, Menu

from enthought.pyface.workbench.action.set_active_perspective_action \
    import SetActivePerspectiveAction


from enthought.pyface.workbench.action.workbench_action import WorkbenchAction

from enthought.envisage.ui.workbench.action.api import \
    ExitAction, EditPreferencesAction, AboutAction

from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

#------------------------------------------------------------------------------
#  "WelcomeAction" class:
#------------------------------------------------------------------------------

#class WelcomeAction(SetActivePerspectiveAction):
#    """ An action that displays the welcome perspective.
#    """
#
#     The action"s name (displayed on menus/tool bar tools etc).
#    name = Str("&Welcome")
#
#     The action"s image (displayed on tool bar tools etc).
#    image = ImageResource("welcome")
#
#     The action's style.
#    style = "push"
#
#    --------------------------------------------------------------------------
#      "SetActivePerspectiveAction" interface:
#    --------------------------------------------------------------------------
#
#    def _perspective_default(self):
#        """ Trait initialiser.
#        """
#        welcome_perspective = self.window.get_perspective_by_id(
#            "envisage.perspective.welcome_perspective")
#
#        return welcome_perspective

#------------------------------------------------------------------------------
#  "WelcomeAction" class:
#------------------------------------------------------------------------------

class WelcomeAction(PyFaceAction):
    """ An action that displays the welcome perspective.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # A longer description of the action.
    description = "Welcome to Envisage"

    # The action"s image (displayed on tool bar tools etc).
    image = ImageResource("welcome")

    # The action"s name (displayed on menus/tool bar tools etc).
    name = "&Welcome"

    # A short description of the action used for tooltip text etc.
    tooltip = "Welcome to Envisage"

    #--------------------------------------------------------------------------
    #  "NewWindowAction" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        welcome_perspective = self.window.get_perspective_by_id(
            "envisage.perspective.welcome_perspective")

        self.window.active_perspective = welcome_perspective


welcome_action = Action(
    path        = "MenuBar/Help",
    class_name  = __name__ + '.WelcomeAction',
    name        = "Welcome",
    group       = "WelcomeGroup",
)

#------------------------------------------------------------------------------
#  "EnvisageActionSet" class:
#------------------------------------------------------------------------------

class EnvisageActionSet(ActionSet):
    """ The default action set for the Envisage plugin.
    """
    menus = [Menu(name="&Help", path="MenuBar",
                groups=["WelcomeGroup", "AboutGroup"], after="Tools")]

    actions = [welcome_action]

# EOF -------------------------------------------------------------------------
