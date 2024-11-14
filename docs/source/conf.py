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

# # Configure search settings
# html_search_language = "th"
# html_search_options = {"type": "default", "dict": None}


# # Add custom search tokenizer
# def thai_tokenizer(content):
#     return word_tokenize(content, engine="newmm")


# def setup(app):
#     if hasattr(app, "add_search_language"):
#         # Register the tokenizer as a class
#         class ThaiSearchLanguage:
#             lang = "th"
#             language_name = "Thai"
#             js_splitter_code = """
#             function(str) {
#                 // Simple word boundary split for Thai
#                 return str.split(/[\\s\\u0E00-\\u0E7F]+/).filter(function(w) { return w.length > 0; });
#             }
#             """
#             js_stemmer_rawcode = """
#             var JSX={};
#             (function(j){
#                 j.stemmer=function(word){
#                     return word;
#                 }
#             })(JSX);
#             """

#             def __init__(self, options):
#                 self.options = options

#             def split(self, s):
#                 return thai_tokenizer(s)

#             def word_context(self, word):
#                 return word

#             @staticmethod
#             def word_filter(word):
#                 # Filter out words that are too short or contain non-Thai characters
#                 if len(word) < 2:
#                     return False
#                 # Check if the word contains at least one Thai character
#                 return any("\u0E00" <= c <= "\u0E7F" for c in word)

#             @staticmethod
#             def stem(word):
#                 # Thai doesn't use stemming, return the word as-is
#                 return word

#         app.add_search_language(ThaiSearchLanguage)
