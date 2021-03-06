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

""" Defines a resource editor for the resource plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import getmtime, dirname

import pickle as pickle

from enthought.traits.api import \
    HasTraits, Instance, Property, Bool, DelegatesTo, AdaptsTo, Str, Float

from enthought.traits.ui.api import View, Item
from enthought.pyface.api import ImageResource, confirm, YES
from enthought.pyface.workbench.api import TraitsUIEditor

from i_resource import IResource

#------------------------------------------------------------------------------
#  "ResourceEditor" class:
#------------------------------------------------------------------------------

class ResourceEditor(TraitsUIEditor):
    """ An editor with content provided by a workspace resource.
    """

    # Is the object that the editor is editing 'dirty' i.e., has it been
    # modified but not saved?
#    dirty = DelegatesTo("editor_input")

#    # The object that the editor is editing. The framework sets this when
#    # the editor is created.
    editor_input = AdaptsTo(IResource)

    # The time of the last modification to the resource.
    m_time = Float

    # An optional reference to the currently selected object in the editor.
    # Used by the properties view.
    selected = Instance(HasTraits)

    # The default view:
#    traits_view = View(Item("editor_input"))

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface:
    #--------------------------------------------------------------------------

    def create_ui(self, parent):
        """ Creates the traits UI that represents the editor.
        """
        self.document = input = self.editor_input.load()
        ui = input.edit_traits(parent=parent, kind="subpanel")

        return ui

    #--------------------------------------------------------------------------
    #  "ResourceEditor" interface:
    #--------------------------------------------------------------------------

    def save(self):
        """ Saves the editor content.
        """
        self.editor_input.save(self.document)
        self.dirty = False


    def save_as(self):
        """ Saves the editor content to a new file name.
        """
        dialog = FileDialog( action   = "save as",
                             wildcard = "All Files (*.*)|*.*",
                             default_directory = dirname(self.obj.path) )

        if dialog.open() == OK:
            self.obj.path = dialog.path
            self.save()

        del dialog

    #--------------------------------------------------------------------------
    #  Private interface:
    #--------------------------------------------------------------------------

    def _editor_input_default(self):
        """ Trait initialiser.
        """
        return self.obj


    def _m_time_default(self):
        """ Trait initialiser.
        """
        if self.obj.exists:
            return getmtime(self.obj.absolute_path)
        else:
            return 0.0


    def _editor_input_changed(self, old, new):
        """ Static trait change handler.
        """
        if old is not None:
            old.on_trait_change(self._set_dirty, remove=True)

        if new is not None:
            new.on_trait_change(self._set_dirty)

        self._set_dirty()


    def _set_dirty(self):
        """ Sets the dirty flag to True.
        """
        self.dirty = True


    def _editor_closing_changed_for_window(self, editor):
        """ Handle the editor being closed.
        """
        if (editor is self) and self.dirty:
            retval = confirm(self.window.control, title="Save Resource",
                message="'%s' has been modified. Save changes?" %
                self.name[1:])

            if retval == YES:
                self.save()


#    def _active_editor_changed_for_window(self, new):
#        """ Handle the active editor changing """
#
#        file = self.obj
#
#        if (new is self) and file.exists \
#        and (self.m_time != getmtime(file.absolute_path)):
#            if self.dirty:
#                name = self.name[1:]
#            else:
#                name = self.name
#
#            retval = confirm(
#                self.window.control, title="Load Resource",
#                message="'%s' has been modified. Load modified resource?" %
#                name
#            )
#
#            if retval == YES:
#                raise NotImplementedError


    def _on_dclick(self, object):
        """ Handle item activation.
        """
        pass


    def _on_select(self, object):
        """ Handle item selection.
        """
        pass


    def _on_modified(self):
        """ Sets the editor dirty when the document is modified.
        """
        self.dirty = True


    def _dirty_fired(self, old, new):
        """ Prepends a '*' to the editor's name when dirty and
            removes it when clean.
        """
        if (old is False) and (new is True):
            self.name = "*" + self.name

        if (old is True) and (new is False):
            if self.name and (self.name[0] == "*"):
                self.name = self.name[1:]
#
#    #--------------------------------------------------------------------------
#    #  "ResourceEditor" interface
#    #--------------------------------------------------------------------------
#
#    def on_name(self, new):
#        """ Handle the object name changing """
#
#        self.name = new


    def on_document_modified(self):
        """ Dirties the editor when the document is modified """

        self.dirty = True


#    def _editor_closing_changed_for_window(self, editor):
#        """ Handle the editor being closed """
#
#        if (editor is self) and self.dirty:
#            retval = confirm(
#                self.window.control, title="Save Resource",
#                message="'%s' has been modified. Save changes?" % self.name[1:]
#            )
#
#            if retval == YES:
#                self.save()
#
#
#    def _active_editor_changed_for_window(self, new):
#        """ Handle the active editor changing """
#
#        file = self.obj
#
#        if (new is self) and file.exists \
#        and (self.m_time != getmtime(file.absolute_path)):
#            if self.dirty:
#                name = self.name[1:]
#            else:
#                name = self.name
#
#            retval = confirm(
#                self.window.control, title="Load Resource",
#                message="'%s' has been modified. Load modified resource?" %
#                name
#            )
#
#            if retval == YES:
#                raise NotImplementedError
##                self.window.edit(self.obj, kind=type(self))
##                self.window.close_editor(new)

# EOF -------------------------------------------------------------------------
