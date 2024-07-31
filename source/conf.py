# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenSRANE Documentation'
copyright = '2023, Bijan Sayyafzadeh'
author = 'Bijan Sayyafzadeh'
release = '0.0.3'
html_logo = 'logo.png'


rst_prolog = """
.. |floatList| replace:: *list float*
.. |integerList| replace:: *list integer*
.. |intList| replace:: *list integer*
.. |listFloat| replace:: *list float*
.. |listInteger| replace:: *list integer*
.. |listInt| replace:: *list integer*
.. |list| replace:: *list*
.. |string| replace:: *string*
.. |float| replace:: *float*
.. |integer| replace:: *integer*
.. |OPR| replace:: `OpenSRANE`_
.. _OpenSRANE: https://github.com/OpenSRANE/OpenSRANE
.. |githubLink| replace:: `OpenSRANE Github`_
.. _OpenSRANE Github: https://github.com/OpenSRANE
.. |doc| replace:: `OpenSRANE Documentation`_
.. _OpenSRANE Documentation: https://opensrane.github.io/OpenSRANE_Documentation/
.. |bsz| replace:: **Bijan Sayyafzadeh**
"""	


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ["_static"]

# import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'analytics_id': 'UA-2431545-1',
	'logo_only': True,
	'prev_next_buttons_location': None,
    'body_max_width': None
}