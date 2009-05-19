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

""" Defines an action for viewing resource properties.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.io.api import File
from enthought.traits.api import Bool, Instance
from enthought.traits.ui.api import View, Item, Group
from enthought.pyface.action.api import Action

#------------------------------------------------------------------------------
#  "PropertiesAction" class:
#------------------------------------------------------------------------------

class PropertiesAction(Action):
    """ Defines an action for viewing resource properties.
    """

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    # The action"s name (displayed on menus/tool bar tools etc):
    name = "P&roperties"

    # Keyboard accelerator:
    accelerator = "Alt+Enter"

    #--------------------------------------------------------------------------
    #  "Action" interface:
    #--------------------------------------------------------------------------

    def perform(self, event):
        """ Perform the action.
        """
        selections = self.window.selection

        if selections:
            selection = selections[0]

            if isinstance(selection, File):
                selection.edit_traits( parent=self.window.control,
                    view=self._create_resource_view(selection),
                    kind="livemodal" )


    def _create_resource_view(self, selection):
        """ Creates a resource view.
        """
        resource_view = View(
            Item(name="absolute_path", style="readonly"),
            # FIXME: Readonly boolean editor is just blank
#            Item(name="exists", style="readonly"),
#            Item(name="is_file", style="readonly"),
#            Item(name="is_folder", style="readonly"),
#            Item(name="is_package", style="readonly"),
#            Item(name="is_readonly", style="readonly"),
            Item(name="mime_type", style="readonly"),
            Item(name="url", style="readonly"),
            title="Properties for %s" % selection.name+selection.ext,
            icon=self.window.application.icon)

        return resource_view

# EOF -------------------------------------------------------------------------
