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
    id = "puddle.workbench"

    #--------------------------------------------------------------------------
    #  WorkbenchApplication interface:
    #--------------------------------------------------------------------------

    # The icon used on window title bars etc.
    icon = ImageResource("frame.ico")

    # The name of the application (also used on window title bars etc).
    name = "Puddle"

    # The default position of the main window.
    window_position = Tuple((60, 60))

    # The default size of the main window.
    window_size = Tuple((800, 600))


    def _about_dialog_default(self):
        """ Trait initialiser.
        """
        about_dialog = AboutDialog(
            parent=self.workbench.active_window.control,
            image=ImageResource("splash"),
            additions=["Richard W. Lincoln &copy; MMIX"],
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
