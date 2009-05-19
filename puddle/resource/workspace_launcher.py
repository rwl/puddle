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
    app_name = Str("Puddle")

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
