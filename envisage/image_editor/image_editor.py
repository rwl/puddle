#------------------------------------------------------------------------------
#
#  Copyright (c) 2009, Richard W. Lincoln
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Author: Richard W. Lincoln
#  Date:   09/05/2009
#
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
            id="envisage.image_editor.image_editor",
            kind="live", resizable=True)

        ui = self.edit_traits(view=view, parent=parent, kind="subpanel")

        return ui

# EOF -------------------------------------------------------------------------
