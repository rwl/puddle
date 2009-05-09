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

""" Defines the workbench application.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import dirname

from enthought.traits.api import Tuple

from enthought.envisage.ui.workbench.api import WorkbenchApplication

from enthought.pyface.api import ImageResource, SplashScreen

from enthought.etsconfig.api import ETSConfig

if ETSConfig.toolkit == "wx":
    from wx_about_dialog import AboutDialog
elif ETSConfig.toolkit == "qt4":
    from qt_about_dialog import AboutDialog
else:
    from enthought.pyface.api import AboutDialog

#------------------------------------------------------------------------------
#  "WorkbenchApplication" class:
#------------------------------------------------------------------------------

class WorkbenchApplication(WorkbenchApplication):
    """ Defines the workbench application.
    """

    #--------------------------------------------------------------------------
    #  IApplication interface:
    #--------------------------------------------------------------------------

    # The application's globally unique Id.
    id = "envisage.workbench"

    #--------------------------------------------------------------------------
    #  WorkbenchApplication interface:
    #--------------------------------------------------------------------------

    # The icon used on window title bars etc.
    icon = ImageResource("frame.ico")

    # The name of the application (also used on window title bars etc).
    name = "Envisage"

    # The default position of the main window.
    window_position = Tuple((0, 0))

    # The default size of the main window.
#    window_size = Tuple((1024, 768))
    window_size = Tuple((1024, 768))


    def _about_dialog_default(self):
        """ Trait initialiser.
        """
        about_dialog = AboutDialog(
            parent=self.workbench.active_window.control,
            image=ImageResource("splash"),
            additions=["@see:  Tango Icon Library"],
        )

        return about_dialog


    def _splash_screen_default(self):
        """ Trait initialiser.
        """
        splash_screen = SplashScreen(
            image=ImageResource("splash"), show_log_messages=False,
            text_color="black"#, text_font="10 point Monospace"
        )

        return splash_screen

# EOF -------------------------------------------------------------------------
