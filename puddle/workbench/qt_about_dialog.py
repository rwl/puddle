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

""" An about dialog derived from the standard qt dialog that does not
    include the copyright notices.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import sys

from enthought.pyface.ui.qt4.about_dialog import AboutDialog as QtAboutDialog

from PyQt4 import QtCore, QtGui

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

# The HTML displayed in the QLabel.
_DIALOG_TEXT = """
<html>
  <body>
    <center>
      <table width="100%%" cellspacing="4" cellpadding="0" border="0">
        <tr>
          <td align="center">
          <p>
            <img src="%s" alt="">
          </td>
        </tr>
      </table>

      <p>
      Python %s<br>
      PyQt %s<br>
      Qt %s<br>
      </p>
      <p>
      %s<br>
      </p>
  </center>
  </body>
</html>
"""

#------------------------------------------------------------------------------
#  "AboutDialog" class:
#------------------------------------------------------------------------------

class AboutDialog(QtAboutDialog):
    """ An about dialog derived from the standard qt dialog that does not
        include the copyright notices.
    """

    #--------------------------------------------------------------------------
    #  Protected "IDialog" interface.
    #--------------------------------------------------------------------------

    def _create_contents(self, parent):
        label = QtGui.QLabel()

        if parent.parent() is not None:
            title = parent.parent().windowTitle()
        else:
            title = ""

        # Set the title.
        self.title = "About %s" % title

        # Load the image to be displayed in the about box.
        image = self.image.create_image()
        path = self.image.absolute_path

        # The additional strings.
        additions = "<br />".join(self.additions)

        # Get the version numbers.
        py_version = sys.version[0:sys.version.find("(")]
        pyqt_version = QtCore.PYQT_VERSION_STR
        qt_version = QtCore.QT_VERSION_STR

        # Set the page contents.
        label.setText(
            _DIALOG_TEXT %
            (path, py_version, pyqt_version, qt_version, additions)
        )

        # Create the button.
        buttons = QtGui.QDialogButtonBox()

        if self.ok_label:
            buttons.addButton(self.ok_label, QtGui.QDialogButtonBox.AcceptRole)
        else:
            buttons.addButton(QtGui.QDialogButtonBox.Ok)

        buttons.connect(
            buttons, QtCore.SIGNAL("accepted()"),
            parent, QtCore.SLOT("accept()")
        )

        lay = QtGui.QVBoxLayout()
        lay.addWidget(label)
        lay.addWidget(buttons)

        parent.setLayout(lay)

# EOF -------------------------------------------------------------------------
