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

""" Defines an action set for the Python editor plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.envisage.ui.action.api import Action, Group, Menu, ToolBar

from enthought.envisage.ui.workbench.api import WorkbenchActionSet

from python_workbench_editor import PythonWorkbenchEditor

#------------------------------------------------------------------------------
#  "PythonEditorActionSet" class:
#------------------------------------------------------------------------------

class PythonEditorActionSet(WorkbenchActionSet):
    """ An action set for the Python editor plug-in.
    """

    #--------------------------------------------------------------------------
    #  "ActionSet" interface:
    #--------------------------------------------------------------------------

    # The action set"s globally unique identifier:
    id = "puddle.python_editor.action_set"

    menus = [
        Menu(
            name="&File", path="MenuBar",
            groups=[
                "OpenGroup", "CloseGroup", "SaveGroup",
                "ImportGroup", "ResourceGroup", "ExitGroup"
            ]
        ),
        Menu(
            name="&New", path="MenuBar/File", group="OpenGroup",
            groups=["ContainerGroup", "ComponentGroup", "OtherGroup"]
        ),
        Menu(
            name="&Tools", path="MenuBar", before="Help",
            groups=["RunGroup", "IPythonShellGroup"]
        ),
        Menu(
            name="&Run As", path="Resource", group="SubMenuGroup",
            groups=["RoutineGroup"]
        )
    ]

    actions = [
        Action(
            path="MenuBar/File/New", group="ComponentGroup",
            class_name="puddle.python_editor.new_file_action:"
            "NewFileAction"
        ),
        Action(
            path="MenuBar/File", group="OpenGroup",
            class_name="puddle.python_editor.open_file_action:"
            "OpenFileAction"
        ),
        Action(
            name="File", path="Workspace/New", group="ComponentGroup",
            id="puddle.python_editor.new_file_action",
            class_name="puddle.python_editor.new_file_action:"
            "NewFileAction"
        ),
        Action(
            path="MenuBar/Tools", group="RunGroup",
            class_name="puddle.python_editor.python_run_action:"
            "PythonRunAction"
        ),
        Action(
            path="Resource/Run As", group="RoutineGroup",
            class_name="puddle.python_editor.python_run_action:"
            "PythonRunAction"
        )
    ]

# EOF -------------------------------------------------------------------------
