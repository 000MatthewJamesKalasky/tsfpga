# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the tsfpga project.
# https://tsfpga.com
# https://gitlab.com/tsfpga/tsfpga
# --------------------------------------------------------------------------------------------------

"""
Configuration file for the Sphinx documentation builder.
"""

from pathlib import Path
import sys

# Do PYTHONPATH insert() instead of append() to prefer any local repo checkout over any pip install
TSFPGA_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(TSFPGA_ROOT))
PATH_TO_HDL_REGISTERS = TSFPGA_ROOT.parent.resolve() / "hdl_registers"
sys.path.insert(0, str(PATH_TO_HDL_REGISTERS))
PATH_TO_VUNIT = TSFPGA_ROOT.parent.parent / "vunit" / "vunit"
sys.path.insert(0, str(PATH_TO_VUNIT.resolve()))

project = "tsfpga"
copyright = "Lukas Vik"
author = "Lukas Vik"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "sphinx_sitemap",
]

# Types that are used but sphinx cant find, because they are external
nitpick_ignore = [
    ("py:class", "vunit.test.report.TestReport"),
    ("py:class", "vunit.test.report.TestResult"),
    ("py:class", "vunit.test.runner.TestRunner"),
    ("py:class", "Register"),
    ("py:class", "RegisterList"),
    ("py:meth", "Register.get_field"),
    ("py:meth", "RegisterArray.get_register"),
    ("py:meth", "RegisterList.create_html_register_table"),
    ("py:meth", "RegisterList.create_html_constant_table"),
    ("py:meth", "RegisterList.create_python_class"),
    ("py:meth", "RegisterList.create_vhdl_package"),
    ("py:meth", "RegisterList.get_constant"),
    ("py:meth", "RegisterList.get_register"),
    ("py:meth", "RegisterList.get_register_array"),
    ("py:meth", "RegisterList.get_register_index"),
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Base URL for generated sitemap XML
html_baseurl = "https://tsfpga.com"

# Include robots.txt which points to sitemap
html_extra_path = ["robots.txt"]

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "prev_next_buttons_location": "both",
}

html_context = {
    "display_gitlab": True,
    "gitlab_user": "tsfpga",
    "gitlab_repo": "tsfpga",
    "gitlab_version": "master",
    "conf_py_path": "/doc/sphinx/",
}


# Make autodoc include __init__ class method.
# https://stackoverflow.com/a/5599712


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
