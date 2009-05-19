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

""" The 'Open With' menu.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.pyface.action.api import Group, MenuManager
from enthought.traits.api import Any, Bool, Instance, List, Str, Unicode
from enthought.traits.api import on_trait_change
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from envisage.resource.action.open_with_action import OpenWithAction

from puddle.resource.resource_plugin import EDITORS

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "OpenWithMenuManager" class:
#------------------------------------------------------------------------------

class OpenWithMenuManager(MenuManager):
    """ The 'Open With' menu.
    """

    #--------------------------------------------------------------------------
    #  "ActionManager" interface
    #--------------------------------------------------------------------------

    # All of the groups in the manager.
    groups = List(Group)

    # The manager"s unique identifier (if it has one).
    id = Str("OpenWith")

    #--------------------------------------------------------------------------
    #  "MenuManager" interface
    #--------------------------------------------------------------------------

    # The menu manager"s name (if the manager is a sub-menu, this is what its
    # label will be).
    name = Unicode("Open With")

    #--------------------------------------------------------------------------
    #  "OpenWithMenuManager" interface
    #--------------------------------------------------------------------------

    # The workbench window that the menu is part of.
    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "ActionManager" interface
    #--------------------------------------------------------------------------

    def _groups_default(self):
        """ Trait initialiser.
        """
        app = self.window.application
        editors = [factory() for factory in app.get_extensions(EDITORS)]

        editors_group = Group(id="editors")

        for editor in editors:
            action = OpenWithAction(editor=editor, window=self.window)
            editors_group.append(action)

        return [editors_group]

# EOF -------------------------------------------------------------------------
