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

""" Resource plug-in actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.io.api import File
from enthought.traits.api import Bool, Str, List, Delegate, Instance
from enthought.pyface.action.api import Action
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from envisage.resource.editor import Editor

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "OpenWithAction" class:
#------------------------------------------------------------------------------

class OpenWithAction(Action):
    """ Defines an action that opens the current resource.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # The action"s name (displayed on menus/tool bar tools etc):
    name = Delegate("editor")

    # The action's image (displayed on tool bar tools etc):
    image = Delegate("editor")

    # Is the action enabled?
    enabled = Bool(True)

    # Is the action visible?
    visible = Bool(True)

    #--------------------------------------------------------------------------
    #  "OpenWithAction" interface:
    #--------------------------------------------------------------------------

    # The workbench window that the menu is part of.
    window = Instance(WorkbenchWindow)

    # The editor extension
    editor = Instance(Editor)

    #--------------------------------------------------------------------------
    #  "OpenWithAction" interface:
    #--------------------------------------------------------------------------

    def _selection_changed_for_window(self, new):
        """ Makes the action visible if a File with a valid extension
            is selected
        """
        if len(new) == 1:
            sel = new[0]

            if isinstance(sel, File) and (sel.ext in self.editor.extensions):
                    self.enabled = True
            else:
                self.enabled = False
        else:
            self.enabled = False

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def _enabled_default(self):
        """ Trait initialiser.
        """
        if self.window.selection:
            sel = self.window.selection[0]

            if isinstance(sel, File) and (sel.ext in self.editor.extensions):
                return True
            else:
                return False
        else:
            return False


    def perform(self, event):
        """ Performs the action.
        """
        selections = self.window.selection
        if selections:
            # Use the first of the selected objects
            selection = selections[0]

            app = self.window.application
            editor = app.import_symbol(self.editor.editor_class)
            self.window.edit(selection, editor)

# EOF -------------------------------------------------------------------------
