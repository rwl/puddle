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

""" Defines the Envisage welcome view.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists, dirname, join
from enthought.traits.api import Instance, File, Event
from enthought.traits.ui.api import View, Item, TreeEditor
from enthought.pyface.image_resource import ImageResource
from enthought.pyface.workbench.api import View as WorkbenchView
from enthought.enable.api import Viewport, Canvas, Component, Pointer
from enthought.enable.component_editor import ComponentEditor
from enthought.kiva.backend_image import Image as KivaImage

#------------------------------------------------------------------------------
#  "Image" class:
#------------------------------------------------------------------------------

class Image(Component):
    """ Defines an image component.
    """
    image_file = File

    #---------------------------------------------------------------------------
    #  Draw component on the graphics context:
    #---------------------------------------------------------------------------

    def _draw_mainlayer(self, gc, view_bounds=None, mode="default"):

        if exists(self.image_file):
            gc.save_state()

            img = KivaImage(self.image_file)

            w, h = img.width(), img.height()
            self.bounds = [w, h]
            gc.draw_image(img, (self.x, self.y, w, h))

            gc.restore_state()

#------------------------------------------------------------------------------
#  "RelativeImage" class:
#------------------------------------------------------------------------------

class RelativeImage(Component):
    """ Defines an image component.
    """
    normal_pointer = Pointer("arrow")
    hover_pointer = Pointer("hand")

    image_file = File#(filter="Image Files (*.png, *.jpg, *.gif)|" \
#        "*.png;*.jpg;*.gif|All Files (*.*)|*.*")

    selected = Event

    #---------------------------------------------------------------------------
    #  Draw component on the graphics context:
    #---------------------------------------------------------------------------

    def _draw_mainlayer(self, gc, view_bounds=None, mode="default"):

        if exists(self.image_file):
            gc.save_state()

    #        self.image_file.seek(0)
            img = KivaImage(self.image_file)

            x = gc.width() * 0.7
            y = gc.height() * 0.15
            w, h = img.width(), img.height()

            # Use Image's ability to draw itself onto a gc to paint the window.
            gc.draw_image(img, (x, y, w, h))

            self.position = [x, y]
            self.bounds = [w, h]

            gc.restore_state()


    def hover_left_down(self, event):
        """ Handles left mouse button clicks in 'normal' mode.
        """
        self.selected = True


    def normal_mouse_enter(self, event):
        """ Handles the mouse entering the component in 'normal' mode.
        """
        self.event_state = "hover"
        event.window.set_pointer(self.hover_pointer)
#        event.window.set_mouse_owner(self, event.net_transform())
        event.handled = True


    def hover_mouse_leave(self, event):
        """ Handles the mouse leaving the component in 'normal' mode.
        """
        self.event_state = "normal"
        event.window.set_pointer(self.normal_pointer)
#        event.window.set_mouse_owner(None)
        event.handled = True
        self.request_redraw()

#------------------------------------------------------------------------------
#  "WelcomeView" class:
#------------------------------------------------------------------------------

class WelcomeView(WorkbenchView):
    """ Defines the Envisage welcome view.
    """

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    # The view's globally unique identifier:
    id = "envisage.welcome_view"

    # The view's name:
    name = "Welcome"

    # The default position of the view relative to the item specified in the
    # "relative_to" trait:
    position = "left"

    # An image used to represent the view to the user (shown in the view tab
    # and in the view chooser etc).
    image = ImageResource("welcome")

    # The width of the item (as a fraction of the window width):
    width = 1.0

    # The category sed to group views when they are displayed to the user:
    category = "General"

    #--------------------------------------------------------------------------
    #  "WelcomeView" interface:
    #--------------------------------------------------------------------------

    canvas = Instance(Canvas)

    # A view into a sub-region of the canvas.
    viewport = Instance(Viewport, desc="canvas sub-region view")

    #--------------------------------------------------------------------------
    #  "IView" interface:
    #--------------------------------------------------------------------------

    def create_control(self, parent):
        """ Create the view contents.
        """
        ui = self.edit_traits(parent=parent, view=self._create_view(),
            kind="subpanel")

        return ui.control

    #--------------------------------------------------------------------------
    #  "WelcomeView" interface:
    #--------------------------------------------------------------------------

    def _canvas_default(self):
        """ Trait initialiser.
        """

        logo_path = join(dirname(__file__), "images", "energy.png")
        logo = Image(image_file=logo_path, bounds=[233, 100],
            position=[20, 20])

        workbench_path = join(dirname(__file__), "images",
            "folder-development.png")
        workbench = RelativeImage(image_file=workbench_path, bounds=[128, 128])
        workbench.on_trait_change(self._on_workbench, "selected")

        canvas = Canvas(bgcolor="white", show_axes=True)
        canvas.add(logo)
        canvas.add(workbench)

        return canvas


    def _viewport_default(self):
        """ Trait initialiser.
        """
        vp = Viewport(component=self.canvas)

        vp.enable_zoom=False
        vp.view_position = [-5, -5]

        return vp


    def _create_view(self):
        """ Create a view with a component editor.
        """
        view = View(Item(name="viewport", show_label=False,
            editor=ComponentEditor()))

        return view


    def _on_workbench(self):
        """ Handle selection of the workbench option.
        """
        welcome_perspective = self.window.get_perspective_by_id(
            "envisage.perspective.default_perspective")

        self.window.active_perspective = welcome_perspective

# EOF -------------------------------------------------------------------------
