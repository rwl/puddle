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

""" Customised 'View' ('Window') menu.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Str, Unicode
from enthought.pyface.action.api import Group, MenuManager
from enthought.pyface.workbench.action.api import ViewMenuManager
from enthought.pyface.workbench.action.perspective_menu_manager import \
    PerspectiveMenuManager

from workbench_action import \
    NewWindowAction, NewEditorAction, PreferencesAction

#------------------------------------------------------------------------------
#  "ViewMenuManager" class:
#------------------------------------------------------------------------------

class ViewMenuManager(ViewMenuManager):
    """ Customised "View" ("Window") menu.
    """

    #--------------------------------------------------------------------------
    #  "ActionManager" interface:
    #--------------------------------------------------------------------------

    # The manager's unique identifier (if it has one).
    id = Str("Window")

    #--------------------------------------------------------------------------
    #  "MenuManager" interface:
    #--------------------------------------------------------------------------

    # The menu manager's name (if the manager is a sub-menu, this is what its
    # label will be).
    name = Unicode("&Window")

    #--------------------------------------------------------------------------
    #  "ActionManager" interface:
    #--------------------------------------------------------------------------

    def _groups_default(self):
        """ Trait initialiser.
        """
#        groups = super(PylonViewMenuManager, self)._groups_default()

        groups = []

        new_group = Group(id="NewGroup")
        new_group.append(NewWindowAction(window=self.window))
        # FIXME: Changing the enabled trait of the NewEditorAction causes barf
#        new_group.append(NewEditorAction(window=self.window))
        # Insert a group for new part actions
        groups.append(new_group)

        # Add a group for view and perspective sub menus
        submenu_group = Group(id="SubMenuGroup")

        # Add the perspective menu (if requested).
        if self.show_perspective_menu and len(self.window.perspectives) > 0:
            perspective_menu = PerspectiveMenuManager(window=self.window)
            submenu_group.append(perspective_menu)

        # TODO: Create a ViewMenuManager with a selection of views
        view_submenu = MenuManager(self._create_other_group(self.window),
            name="Show View")
        submenu_group.append(view_submenu)
        groups.append(submenu_group)

        # Add a group containing a 'toggler' for all visible views.
        self._view_group = self._create_view_group(self.window)
        groups.append(self._view_group)

        # Add a group containing the preferences action
        groups.append( Group(PreferencesAction(window=self.window)) )

        return groups

# EOF -------------------------------------------------------------------------
