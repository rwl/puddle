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

from setuptools import setup, find_packages

setup(
    author="Richard W. Lincoln",
    author_email="r.w.lincoln@gmail.com",
    description="Resource plug-in for Envisage.",
    url="http://rwl.github.com/resource",
    version="0.1",
    install_requires=["EnvisageCore>=3.0.2", "EnvisagePlugins>=3.0.2"],
    license="GPLv2",
    name="Resource Plug-in",
    include_package_data=True,
    packages=find_packages(),
#    namespace_packages=[],
    zip_safe=False
)

# EOF -------------------------------------------------------------------------
