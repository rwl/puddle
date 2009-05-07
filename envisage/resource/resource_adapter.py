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

""" An editor with content provided by a workspace resource.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import pickle as pickle

from os.path import getmtime

from enthought.io.api import File

from enthought.traits.api import \
    Interface, Property, Bool, Adapter, AdaptedTo, AdaptsTo, DelegatesTo, \
    adapts, Instance, Float, HasTraits

from enthought.traits.ui.api import View, Item, Group

from enthought.pyface.workbench.api import TraitsUIEditor

#------------------------------------------------------------------------------
#  "IResource" class:
#------------------------------------------------------------------------------

class IResource(Interface):
    """ Interface for resource """

    dirty = Bool(False)

    is_modifiable = Property(Bool)

    is_readonly = Property(Bool)

    def save(self, file):
        """ Save the object to a file """

    def load(self, file):
        """ Load the object from a file """

    def _get_is_modifiable(self):
        """ Property getter """

    def _get_is_readonly(self):
        """ Property getter """

#------------------------------------------------------------------------------
#  "PickleFileIResourceAdapter" class:
#------------------------------------------------------------------------------

class PickleFileIResourceAdapter(Adapter):
    """ Adapts a "File" with pickled content to 'IResource'.
    """
    # Declare the interfaces this adapter implements for its client:
    adapts(File, to=IResource, when="adaptee.ext=='.pkl'")

    # The object that is being adapted.
    adaptee = Instance(File)

    # Is the object 'dirty'?
#    dirty = Bool(False)

    # The time of the last modification
#    m_time = Float

    def save(self, obj):
        """ Save to file """

        fd = None
        try:
            fd = open(self.adaptee.absolute_path, "wb")
            pickle.dump(obj, fd)
        finally:
            if fd is not None:
                fd.close()

#        self.m_time = getmtime(self.adaptee.absolute_path)


    def load(self):
        """ Load the file """

        fd = None
        try:
            fd = open(self.adaptee.absolute_path, "rb")
            obj = pickle.load(fd)
        finally:
            if fd is not None:
                fd.close()

        return obj

#------------------------------------------------------------------------------
#  "ResourceEditor" class:
#------------------------------------------------------------------------------

class ResourceEditor(TraitsUIEditor):
    """ An editor with content provided by a workspace resource """

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
    traits_view = View(Item("editor_input"))

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface:
    #--------------------------------------------------------------------------

    def create_ui(self, parent):
        """ Creates the traits UI that represents the editor """

        input = self.editor_input.load()

        ui = self.edit_traits(
            parent=parent, view=self.view, kind="subpanel"
        )

        return ui

    #--------------------------------------------------------------------------
    #  "ResourceEditor" interface:
    #--------------------------------------------------------------------------

    def save(self):
        """ Saves the editor content """

        self.editor_input.save()


    def save_as(self):
        """ Saves the editor content to a new file name """

        self.save

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
        """ Static trait change handler """

        if old is not None:
            old.on_trait_change(self._set_dirty, remove=True)

        if new is not None:
            new.on_trait_change(self._set_dirty)

        self._set_dirty()


    def _set_dirty(self):
        """ Sets the dirty flag to True """

        self.dirty = True


    def _editor_closing_changed_for_window(self, editor):
        """ Handle the editor being closed """

        if (editor is self) and self.dirty:
            retval = confirm(
                self.window.control, title="Save Resource",
                message="'%s' has been modified. Save changes?" % self.name[1:]
            )

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
        """ Handle item activation """

        pass


    def _on_select(self, object):
        """ Handle item selection """

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

# EOF -------------------------------------------------------------------------
