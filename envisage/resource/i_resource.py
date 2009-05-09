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

""" Defines the resource interface.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api import Interface, Property, Bool

#------------------------------------------------------------------------------
#  "IResource" class:
#------------------------------------------------------------------------------

class IResource(Interface):
    """ Interface for resource.
    """

    dirty = Bool(False)

    is_modifiable = Property(Bool)

    is_readonly = Property(Bool)

    def save(self, file):
        """ Save the object to a file.
        """

    def load(self, file):
        """ Load the object from a file.
        """

    def _get_is_modifiable(self):
        """ Property getter.
        """

    def _get_is_readonly(self):
        """ Property getter.
        """

# EOF -------------------------------------------------------------------------
