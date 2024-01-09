# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Monografia'
copyright = '2023, Sphinx'
author = 'Leonardo Belintani'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = ['sphinx.ext.mathjax']


templates_path = ['_templates']
exclude_patterns = []

html_title = "Página Inicial"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'

#html_css_files = ['custom.css',]




