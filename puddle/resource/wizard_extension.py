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

""" Defines a wizard extension to the workspace plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.traits.api import HasTraits, Instance, Str, List
from enthought.pyface.api import ImageResource

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "WizardExtension" class:
#------------------------------------------------------------------------------

class WizardExtension(HasTraits):
    """ Defines a wizard extension to the resource plug-in.
    """

    # The wizard contribution's globally unique identifier.
    id = Str

    # Human readable identifier
    name = Str

    # The wizards's image (displayed on selection etc)
    image = Instance(ImageResource)

    # The class of contributed wizard
    wizard_class = Str

    # A longer description of the wizard's function
    description = Str

    def _id_default(self):
        """ Trait initialiser.
        """
        id = "%s.%s" % (type(self).__module__, type(self).__name__)
        logger.warn( "wizard contribution %s has no Id - using <%s>" %
            (self, id) )

        return id

# EOF -------------------------------------------------------------------------
