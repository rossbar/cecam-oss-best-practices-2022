# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ESSD Tools and Best-Practices Panel Discussion'
copyright = '2022, Ross Barnowski, Rohit Goswami'
author = 'Ross Barnowski, Rohit Goswami'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',  # built-in ignores
    'presentation.ipynb',  # Use the markdown-formatted notebook instead
    'cecam-env/*',  # ignore virtualenv
    'README.md'  # not part of website
]

# Ignore myst warnings about non-consecutive headers
suppress_warnings = ["myst.header"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
