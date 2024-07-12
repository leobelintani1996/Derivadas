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
extensions = ['sphinx.ext.autosectionlabel']
# Adicione sphinx.ext.githubpages à lista de extensões
extensions = [
    'sphinx.ext.githubpages',
    # inclua aqui outras extensões que você já está usando
]



templates_path = ['_templates']
exclude_patterns = []

html_title = "Página Inicial"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'




# This is used by Sphinx in many places, such as page title tags.
project = "Monografia"

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "TCC - Leonardo Belintani",
    logo = "Logomarca_UFSCAR.svg",
    logo_alt = "",
    logo_height = 150,
    logo_url = "",
    logo_width = 150,
    github_url = "https://github.com/leobelintani1996/Derivadas",
    
)





