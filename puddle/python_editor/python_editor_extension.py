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

""" Python editor extensions """

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path import dirname

from enthought.pyface.api import ImageResource
from puddle.resource.editor import Editor

#------------------------------------------------------------------------------
#  "PythonEditorExtension" class:
#------------------------------------------------------------------------------

class PythonEditorExtension(Editor):
    """ Associates a Python editor with *.py files.
    """
    # The object contribution's globally unique identifier.
    id = "puddle.python_editor"

    # A name that will be used in the UI for this editor
    name = "Python Editor"

    # An icon that will be used for all resources that match the
    # specified extensions
    image = ImageResource("python")

    # The contributed editor class
    editor_class = "puddle.python_editor.python_workbench_editor:" \
        "PythonWorkbenchEditor"

    # The list of file types understood by the editor
    extensions = [".py"]

    # If true, this editor will be used as the default editor for the type
    default = False

#------------------------------------------------------------------------------
#  "TextEditorExtension" class:
#------------------------------------------------------------------------------

class TextEditorExtension(Editor):
    """ Associates a text editor with *.py files.
    """

    # The object contribution's globally unique identifier.
    id = "puddle.python_editor.text_editor_extension"

    # A name that will be used in the UI for this editor
    name = "Text Editor"

    # An icon that will be used for all resources that match the
    # specified extensions
    image = ImageResource("python")

    # The contributed editor class
    editor_class = "enthought.plugins.text_editor.editor.text_editor:" \
        "TextEditor"

    # The list of file types understood by the editor
    extensions = [".py"]

    # If true, this editor will be used as the default editor for the type
    default = True

# EOF -------------------------------------------------------------------------
