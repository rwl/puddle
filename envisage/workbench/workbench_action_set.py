#------------------------------------------------------------------------------
# Copyright (C) 2007 Richard W. Lincoln
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

""" Workbench plug-in with custom actions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.envisage.ui.action.api import Action, ActionSet, Menu, ToolBar

#------------------------------------------------------------------------------
#  "WorkbenchActionSet" class:
#------------------------------------------------------------------------------

class WorkbenchActionSet(ActionSet):
    """ A custom workbench action set.
    """
    menus = [
        Menu(
            name="&File", path="MenuBar",
            groups=[
                "OpenGroup", "CloseGroup", "SaveGroup",
                "ImportGroup", "ExitGroup"
            ]
        ),
        Menu(
            name="&Edit", path="MenuBar", after="File",
            groups=["UndoGroup", "ClipboardGroup", "PreferencesGroup"]
        ),
        Menu(
            path="MenuBar",
#            class_name="enthought.pyface.workbench.action.api:ViewMenuManager"
            class_name="envisage.workbench.view_menu_manager:"
            "ViewMenuManager",
            before="Help"
        ),
        Menu(name="&Tools", path="MenuBar", groups=["PreferencesGroup"]),
        Menu(name="&Help", path="MenuBar", groups=["AboutGroup"])
    ]

#    tool_bars = [
#        ToolBar(
#            name="Workbench", groups=["WorkbenchGroup", "FileGroup"],
#            id="enthought.envisage.ui.workbench.toolbar"
#        )
#    ]

    actions = [
        Action(
            path="MenuBar/File", group="ExitGroup",
            class_name="envisage.workbench.workbench_action:"
            "ExitAction"
        ),
#        Action(
#            path="ToolBar/Workbench", group="WorkbenchGroup",
#            class_name="envisage.workbench.workbench_action:"
#            "ExitAction"
#        ),
#        Action(
#            path="MenuBar/Edit",
#            class_name="envisage.workbench.workbench_action:"
#            "UndoAction"
#        ),
#        Action(
#            path="MenuBar/Edit", group="PreferencesGroup",
#            class_name="envisage.workbench.workbench_action:"
#            "PreferencesAction"
#        ),
        Action(
            path="MenuBar/Help", group="AboutGroup",
            class_name="envisage.workbench.workbench_action:"
            "AboutAction"
        ),
    ]

# EOF -------------------------------------------------------------------------
