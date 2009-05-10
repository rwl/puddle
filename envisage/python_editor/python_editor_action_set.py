#------------------------------------------------------------------------------
#
#  Copyright (c) 2008, Richard W. Lincoln
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Author: Richard W. Lincoln
#  Date:   14/06/2008
#
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
    id = "envisage.python_editor.action_set"

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
            class_name="envisage.python_editor.new_file_action:"
            "NewFileAction"
        ),
        Action(
            path="MenuBar/File", group="OpenGroup",
            class_name="envisage.python_editor.open_file_action:"
            "OpenFileAction"
        ),
        Action(
            name="File", path="Workspace/New", group="ComponentGroup",
            id="envisage.python_editor.new_file_action",
            class_name="envisage.python_editor.new_file_action:"
            "NewFileAction"
        ),
        Action(
            path="MenuBar/Tools", group="RunGroup",
            class_name="envisage.python_editor.python_run_action:"
            "PythonRunAction"
        ),
        Action(
            path="Resource/Run As", group="RoutineGroup",
            class_name="envisage.python_editor.python_run_action:"
            "PythonRunAction"
        )
    ]

# EOF -------------------------------------------------------------------------
