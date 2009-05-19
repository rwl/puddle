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

""" wxPython specific about dialog derived from the pyface dialog, but
    no Enthought copyright notice.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import sys

import wx
import wx.html
import wx.lib.wxpTag

from enthought.pyface.ui.wx.about_dialog import AboutDialog \
    as EnthoughtAboutDialog

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

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
      wxPython %s<br>
      </p>
      <p>
      %s<br>
      </p>

      <p>
        <wxp module="wx" class="Button">
          <param name="label" value="%s">
          <param name="id"    value="ID_OK">
        </wxp>
      </p>
  </center>
  </body>
</html>
"""

#------------------------------------------------------------------------------
#  "AboutDialog" class:
#------------------------------------------------------------------------------

class AboutDialog(EnthoughtAboutDialog):
    """ wxPython specific about dialog derived from the pyface dialog, but
        no Enthought copyright notice.
    """

    #--------------------------------------------------------------------------
    #  Protected "IDialog" interface.
    #--------------------------------------------------------------------------

    def _create_contents(self, parent):
        if parent.GetParent() is not None:
            title = parent.GetParent().GetTitle()

        else:
            title = ""

        # Set the title.
        self.title = "About %s" % title

        # Load the image to be displayed in the about box.
        image = self.image.create_image()
        path  = self.image.absolute_path

        # The additional strings.
        additions = '<br />'.join(self.additions)

        # The width of a wx HTML window is fixed (and  is given in the
        # constructor). We set it to the width of the image plus a fudge
        # factor! The height of the window depends on the content.
        width = image.GetWidth() + 80
        html = wx.html.HtmlWindow(parent, -1, size=(width, -1))

        # Get the version numbers.
        py_version = sys.version[0:sys.version.find("(")]
        wx_version = wx.VERSION_STRING

        # Get the text of the OK button.
        if self.ok_label is None:
            ok = "OK"
        else:
            ok = self.ok_label

        # Set the page contents.
        html.SetPage(
            _DIALOG_TEXT % (path, py_version, wx_version, additions, ok)
        )

        # Make the 'OK' button the default button.
        ok_button = html.FindWindowById(wx.ID_OK)
        ok_button.SetDefault()

        # Set the height of the HTML window to match the height of the content.
        internal = html.GetInternalRepresentation()
        html.SetSize((-1, internal.GetHeight()))

        # Make the dialog client area big enough to display the HTML window.
        # We add a fudge factor to the height here, although I'm not sure why
        # it should be necessary, the HTML window should report its required
        # size!?!
        width, height = html.GetSize()
        parent.SetClientSize((width, height + 10))

# EOF -------------------------------------------------------------------------
