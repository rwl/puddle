#------------------------------------------------------------------------------
# Copyright (C) 2007 Richard W. Lincoln
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
    """ Defines a extension to the "editors" extension point of the resource
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
