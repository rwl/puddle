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

""" Defines perspectives for the Envisage plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Tuple

from enthought.pyface.workbench.api import Perspective, PerspectiveItem

#------------------------------------------------------------------------------
#  "WelcomePerspective" class:
#------------------------------------------------------------------------------

class WelcomePerspective(Perspective):
    """ Defines the Envisage welcome perspective.
    """

    # The perspective's unique identifier (unique within a workbench window).
    id = "envisage.perspective.welcome_perspective"

    # The perspective's name.
    name = "Welcome"

    # Is the perspective enabled?
    enabled = True

    # Should the editor area be shown in this perspective:
    show_editor_area = False

    # The contents of the perspective:
    contents = [PerspectiveItem(id="envisage.welcome_view",
                    position="left", width=1.0)]

#------------------------------------------------------------------------------
#  "DefaultPerspective" class:
#------------------------------------------------------------------------------

class DefaultPerspective(Perspective):
    """ Defines the default perspective.
    """

    # The perspective's unique identifier (unique within a workbench window).
    id = "envisage.perspective.default_perspective"

    # The perspective's name.
    name = "Default"

    # The size of the editor area in this perspective. A value of (-1, -1)
    # indicates that the workbench window should choose an appropriate size
    # based on the sizes of the views in the perspective.
    editor_area_size = Tuple((400, 400))

    # Is the perspective enabled?
    enabled = True

    # Should the editor area be shown in this perspective:
    show_editor_area = True

    # The contents of the perspective:
    contents = [
        PerspectiveItem(
            id="envisage.resource.resource_view",
            position="left", width=0.2
        ),
        PerspectiveItem(
            id="enthought.plugins.python_shell_view",
            position="bottom", height=0.2
        ),
        PerspectiveItem(
            id="enthought.logger.plugin.view.logger_view.LoggerView",
            position="with", height=0.2,
            relative_to="enthought.plugins.python_shell_view"
        ),
        PerspectiveItem(
            id="envisage.property_view.property_view",
            position="right", width=0.2,
        ),
        PerspectiveItem(
            id="enthought.plugins.ipython_shell.namespace_view",
            position="with", width=0.2,
            relative_to="envisage.property_view.property_view"
        ),
    ]

# EOF -------------------------------------------------------------------------
