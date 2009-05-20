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

""" Defines a tree view of the workspace for the workbench.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Instance, HasTraits
from enthought.traits.ui.api import View, Item, Label
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.workbench.api import View as WorkbenchView
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

#------------------------------------------------------------------------------
#  "PropertyView" class:
#------------------------------------------------------------------------------

class PropertyView(WorkbenchView):
    """ Defines a workbench view that displays property names and values
        for selected items.
    """

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    # The view's globally unique identifier:
    id = "puddle.property_view.property_view"

    # The view's name:
    name = "Properties"

    # The default position of the view relative to the item specified in the
    # "relative_to" trait:
    position = "right"

    # An image used to represent the view to the user (shown in the view tab
    # and in the view chooser etc).
    image = ImageResource("table")

    # The width of the item (as a fraction of the window width):
    width = 0.2

    # The category sed to group views when they are displayed to the user:
    category = "General"

    #--------------------------------------------------------------------------
    #  "WorkbenchView" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    #--------------------------------------------------------------------------
    #  "PropertyView" interface:
    #--------------------------------------------------------------------------

    selected = Instance(HasTraits)

    traits_view = View(
        Item("selected", style="custom", show_label=False, springy=True),
        scrollable=True)

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    def create_control(self, parent):
        """ Create the view contents.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")

        return ui.control

    #--------------------------------------------------------------------------
    #  "WorkbenchView" interface:
    #--------------------------------------------------------------------------

    def _active_editor_changed_for_window(self, obj, name, old, new):
        """ Adds a static handler to the new editors 'selected'
            trait (if any).
        """

        if hasattr(old, "selected"):
            old.on_trait_change(self.select, "selected", remove=True)
        if hasattr(new, "selected"):
            new.on_trait_change(self.select, "selected")
            self.select(None)
        else:
            self.select(None)


    def select(self, new):
        """ Makes the newly selected object visible in the properties view.
        """
        self.selected = new

# EOF -------------------------------------------------------------------------
