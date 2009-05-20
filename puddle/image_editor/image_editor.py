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

""" Defines a simple image editor.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import exists, basename

from enthought.pyface.workbench.api import TraitsUIEditor
from enthought.traits.api import Code, Instance, Str
from enthought.traits.ui.api import View, Item, Group
from enthought.traits.ui.api import ImageEditor as ImageTraitEditor
from enthought.pyface.image_resource import ImageResource

#------------------------------------------------------------------------------
#  "ImageEditor" class:
#------------------------------------------------------------------------------

class ImageEditor(TraitsUIEditor):
    """ An image editor.
    """

    #--------------------------------------------------------------------------
    #  "ImageEditor" interface:
    #--------------------------------------------------------------------------

    # Some text:
    text = Str("image")

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface.
    #--------------------------------------------------------------------------

    def _name_default(self):
        """ Trait initialiser.
        """
        # 'obj' is a io.File
        self.obj.on_trait_change(self.on_path, "path")

        return basename(self.obj.path)


    def on_path(self, new):
        """ Handle the file path changing.
        """
        self.name = basename(new)


    def create_ui(self, parent):
        """ Creates the toolkit-specific control that represents the
            editor. 'parent' is the toolkit-specific control that is
            the editor's parent.
        """
        view = View(
            Item(name="text",
                show_label=False,
                editor=ImageTraitEditor(
                    image=ImageResource(self.obj.name,
                        search_path=[self.obj.parent.absolute_path]) )),
            id="puddle.image_editor.image_editor",
            kind="live", resizable=True)

        ui = self.edit_traits(view=view, parent=parent, kind="subpanel")

        return ui

# EOF -------------------------------------------------------------------------
