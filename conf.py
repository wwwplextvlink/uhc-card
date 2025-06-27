# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'UnitedHealthcare Activation Guide'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare Help Center'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = []

# -- HTML output settings ----------------------------------------------------
html_title = "How to Activate Your UnitedHealthcare Account – Step-by-Step Guide"
html_short_title = "Activate UHC Account"
html_favicon = 'favicon.ico'
html_theme = 'alabaster'  # Or use 'sphinx_rtd_theme' if installed
html_show_sourcelink = False
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
}

# Optional static paths
# html_static_path = ['_static']
