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

""" Defines an extension to the "editors" extension point of the
    resource plug-in that associates editors with certain file extensions.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.traits.api import HasTraits, Instance, Str, List, Bool
from enthought.pyface.api import ImageResource
from enthought.envisage.ui.action.api import Action

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "Editor" class:
#------------------------------------------------------------------------------

class Editor(HasTraits):
    """ Defines a extension to the 'editors' extension point of the resource
        plug-in that associates editors with certain file extensions.
    """

    # The object contribution's globally unique identifier.
    id = Str

    # A name that will be used in the UI for this editor
    name = Str

    # An icon that will be used for all resources that match the
    # specified extensions
    image = Instance(ImageResource)

    # The contributed editor class
    editor_class = Str

    # The list of file types understood by the editor
    extensions = List(Str)

    # If true, this editor will be used as the default editor for the type
    default = Bool(False)

    #--------------------------------------------------------------------------
    #  Editor interface:
    #--------------------------------------------------------------------------

    def _id_default(self):
        """ Trait initialiser.
        """
        id = "%s.%s" % (type(self).__module__, type(self).__name__)
        logger.warn( "editor %s has no Id - using <%s>" % (self, id) )

        return id

# EOF -------------------------------------------------------------------------
