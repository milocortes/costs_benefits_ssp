# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Costs Benefits Analysis'
copyright = '2025, Centro de Investigación en Ciencia de Decisiones'
author = 'Centro de Investigación en Ciencia de Decisiones'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['sphinxcontrib.bibtex']
extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'
#html_theme = 'sphinxawesome_theme'
#html_static_path = ['_static']

# -- Bibtex --#
#bibtex_bibfiles = ['refs.bib']