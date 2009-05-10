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

""" Defines a WorkspaceLauncher class that may be used to select the
    workspace folder to be used for a particular session.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join, exists

from enthought.traits.api import \
    HasTraits, Directory, Bool, Str, Property, Instance, cached_property

from enthought.traits.ui.api import \
    View, Item, Group, Label, Heading, DirectoryEditor

from enthought.traits.ui.menu import OKCancelButtons

from resource import Workspace

#------------------------------------------------------------------------------
#  "WorkspaceLauncher" class:
#------------------------------------------------------------------------------

class WorkspaceLauncher(HasTraits):
    """ Defines a WorkspaceLauncher class that may be used to select the
        workspace folder to be used for a particular session
    """

    workspace = Instance(Workspace)

    # Workspace folder to use
    workspace_dir = Directory(join(expanduser("~"), "workspace"))

    # Should the selected folder be used as the default and the selection
    # request not be made again?
    default = Bool(False)

    # Are we already using a workspace and changing?
    changing = Bool(False)

    # The name of the application to use in the dialog label
    app_name = Str("Envisage")

    # A label explaining the workspace concept
    _label = Property(Str)

    traits_view = View(
        Group(
            Heading("Select a workspace"),
            Item(name="_label", style="readonly", show_label=False),
            "_"
        ),
        Item(name="workspace", style="custom"),
        Group(
            Item(
                name="default",
                label="Use this as the default and do not ask again",
                visible_when="changing==False"
            ),
            show_left=False
        ),
        title="Workspace Launcher",
        width=0.4,
        buttons=OKCancelButtons
    )

    def _workspace_dir_changed(self):
        """ Handles the selected directory changing.
        """
        pass


    def _workspace_default(self):
        """ Trait initialiser.
        """
        return Workspace(join(expanduser("~"), "workspace"))


    def _get__label(self):
        """ Property getter.
        """
        return "%s stores your projects in a folder " \
            "called a workspace.\nChoose a workspace folder to use " \
            "for this session." % self.app_name

# EOF -------------------------------------------------------------------------
