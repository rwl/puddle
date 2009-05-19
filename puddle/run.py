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

""" Run Puddle with assorted plug-ins.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.envisage.core_plugin import CorePlugin

from enthought.plugins.ipython_shell.ipython_shell_plugin \
    import IPythonShellPlugin as PythonShellPlugin

from enthought.logger.plugin.logger_plugin import LoggerPlugin

from puddle.plugin import PuddlePlugin

from puddle.workbench.workbench_plugin import WorkbenchPlugin
from puddle.workbench.workbench_application import WorkbenchApplication

from puddle.resource.resource_plugin import ResourcePlugin
from puddle.python_editor.python_editor_plugin import PythonEditorPlugin
from puddle.property_view.property_view_plugin import PropertyViewPlugin
from puddle.image_editor.image_editor_plugin import ImageEditorPlugin

#------------------------------------------------------------------------------
#  Logging:
#------------------------------------------------------------------------------

logger = logging.getLogger()
handler = logging.StreamHandler()
#handler = logging.StreamHandler(file("/tmp/resource.log", "w"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

#------------------------------------------------------------------------------
#  "main" function:
#------------------------------------------------------------------------------

def main():
    """ Runs the application.
    """
    application = WorkbenchApplication(
        id = "puddle",
        plugins = [
            CorePlugin(),
            PuddlePlugin(),
            WorkbenchPlugin(),
            ResourcePlugin(),
            PythonShellPlugin(),
            LoggerPlugin(),
            PythonEditorPlugin(),
            PropertyViewPlugin(),
            ImageEditorPlugin()
        ]
    )

    application.run()


if __name__ == "__main__":
    main()

# EOF -------------------------------------------------------------------------
