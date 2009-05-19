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
                "ImportGroup", "ResourceGroup", "ExitGroup"
            ]
        ),
        Menu(
            name="&Edit", path="MenuBar", after="File",
            groups=["UndoGroup", "ClipboardGroup", "PreferencesGroup"]
        ),
        Menu(
            path="MenuBar",
#            class_name="enthought.pyface.workbench.action.api:ViewMenuManager"
            class_name="puddle.workbench.view_menu_manager:"
            "ViewMenuManager",
            before="Help"
        ),
        Menu(name="&Tools", path="MenuBar", groups=["PreferencesGroup"]),
        Menu(name="&Help", path="MenuBar", groups=["AboutGroup"])
    ]

    actions = [
        Action(
            path="MenuBar/File", group="ExitGroup",
            class_name="puddle.workbench.workbench_action:"
            "ExitAction"
        ),
        Action(
            path="MenuBar/Help", group="AboutGroup",
            class_name="puddle.workbench.workbench_action:"
            "AboutAction"
        )
    ]

# EOF -------------------------------------------------------------------------
