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

""" Image editor extensions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.pyface.api import ImageResource
from envisage.resource.editor import Editor

#------------------------------------------------------------------------------
#  "ImageEditorExtension" class:
#------------------------------------------------------------------------------

class ImageEditorExtension(Editor):
    """ Associates an image editor with certain file extensions.
    """

    # The object contribution's globally unique identifier.
    id = "envisage.image_editor"

    # A name that will be used in the UI for this editor
    name = "Image Editor"

    # An icon that will be used for all resources that match the
    # specified extensions
    image = ImageResource("image")

    # The contributed editor class
    editor_class = "envisage.image_editor.image_editor:ImageEditor"

    # The list of file types understood by the editor
    extensions = [".png", ".jpg", ".gif"]

    # If true, this editor will be used as the default editor for the type
    default = True

# EOF -------------------------------------------------------------------------
