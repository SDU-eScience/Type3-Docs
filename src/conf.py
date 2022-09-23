#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Emiliano Molinaro <molinaro@imada.sdu.dk>

import sys, os, re, pygments
from glob import glob
import shutil
import warnings

sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

autosummary_generate = True
autosummary_imported_members = False
automodsumm_inherited_members = True

add_module_names = False

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Type 3 - Large Memory HPC '
copyright = """Copyright 2020-2021, SDU eScience Center"""
author = 'SDU eScience Team'

language = 'en' 

# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.DS_Store']

show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# -- Options for HTML output ----------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Type 3'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = ''

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['extra']

html_sidebars = {
    '**' : [
        'searchbox.html',
        'globaltoc.html',
    ]
}

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# -- UCloud theme ---------------------------------------------------------
html_theme = 'ucloud_theme'
html_theme_path = ['../']

# ucloud theme options (see theme.conf for more information)
html_theme_options = {
    # Set the path to a special layout to include for the homepage
    # "homepage": "special_index.html",

    # Set the name of the project to appear in the left sidebar.
    "project_nav_name": "Type 3",
    # "project_logo": "_static/ucloud_logo.png",
}

# the order in which autodoc lists the documented members
autodoc_member_order = 'bysource'

# inheritance_diagram graphviz attributes
inheritance_node_attrs = dict(color='lightskyblue1', style='filled')
