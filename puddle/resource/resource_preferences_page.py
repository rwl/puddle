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

""" Defines the preferences page for the resource plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import expanduser, join

from enthought.traits.api import Bool, Enum, String, Directory

from enthought.traits.ui.api import \
    View, Group, HGroup, VGroup, Item, Label, Heading

from enthought.preferences.ui.api import PreferencesPage

#------------------------------------------------------------------------------
#  "ResourcePreferencesPage" class:
#------------------------------------------------------------------------------

class ResourcePreferencesPage(PreferencesPage):
    """ Defines the preferences page for the resource plug-in.
    """

    #--------------------------------------------------------------------------
    #  "PreferencesPage" interface:
    #--------------------------------------------------------------------------

    # The page's category (e.g. 'General/Appearance'). The empty string means
    # that this is a top-level page.
    category = "General"

    # The page's help identifier (optional). If a help Id *is* provided then
    # there will be a 'Help' button shown on the preference page.
    help_id = ""

    # The page name (this is what is shown in the preferences dialog.
    name = "Resource"

    # The path to the preferences node that contains the preferences.
    preferences_path = "puddle.resource"

    #--------------------------------------------------------------------------
    #  Preferences:
    #--------------------------------------------------------------------------

    # Prompt for workspace on startup?
#    prompt = Bool(True)

    # The default workspace to use without prompting
    default = Directory(expanduser("~"), exists=False,
        desc="the default workspace directory location")

    # Refresh workspace on startup?
#    refresh = Bool(False)

    #--------------------------------------------------------------------------
    #  Traits UI views:
    #--------------------------------------------------------------------------

    traits_view = View(
        Label("Resource"),
        "_",
#        Group(
#            Item(name="prompt", label="Prompt for workspace on startup."),
#            show_left=False
#        ),
#        Item(name="default", enabled_when="prompt==False", show_label=False),
#        Group(
#            Item(name="refresh", label="Refresh workspace on startup.", enabled_when="False"),
#            show_left=False
#        )
    )

# EOF -------------------------------------------------------------------------
