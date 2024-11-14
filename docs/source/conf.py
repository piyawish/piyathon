from datetime import datetime

# from pythainlp.tokenize import word_tokenize

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Piyathon Documentation"
# pylint: disable=redefined-builtin
copyright = f"{datetime.now().year}, Piyawish Piyawat"
# pylint: enable=redefined-builtin

author = "Piyawish Piyawat"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

# Configure MyST-Parser
myst_enable_extensions = [
    "colon_fence",
]

templates_path = ["_templates"]
exclude_patterns = []

locale_dirs = ["locale/"]
gettext_compact = False
gettext_uuid = True
language = "th"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_logo = "_static/logo.png"
html_title = "ภาษาปิยะทอน (Piyathon Language)"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

# Add these lines to configure theme options
html_theme_options = {
    "sidebar_hide_name": True,
}
