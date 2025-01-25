import os
import sys
from datetime import datetime

# # Add the docs/source directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import and register the Piyathon lexer
import piyathon_lexer  # pylint: disable=unused-import

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ภาษาปิยะธอน (Piyathon)"
# pylint: disable=redefined-builtin
copyright = f"{datetime.now().year}, ปิยะวิชญ์ ปิยะวัฒน์"
# pylint: enable=redefined-builtin

author = "ปิยะวิชญ์ ปิยะวัฒน์"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_sitemap",
    "sphinxext.opengraph",
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

ogp_site_url = "https://www.piyathon.org/"
ogp_image = "https://www.piyathon.org/_static/piyathon-og.png"
ogp_social_cards = {
    "enable": True,
    "font": "Noto Sans Thai",
    "image": "https://www.piyathon.org/_static/piyathon-og.png",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_logo = "_static/logo.png"
html_title = "ภาษาปิยะธอน (Piyathon Language)"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

# Add these lines to configure theme options
html_theme_options = {
    "sidebar_hide_name": True,
}

html_extra_path = ["robots.txt"]

html_baseurl = "https://www.piyathon.org/"
sitemap_url_scheme = "{link}"


# -- Options for PDF output --------------------------------------------------

latex_engine = "xelatex"

latex_elements = {
    "preamble": r"""

\usepackage{fontspec}
\usepackage{xunicode}
\usepackage{xltxtra}
\usepackage{polyglossia}
\setdefaultlanguage[numerals=thai]{thai}
\setotherlanguage{english}

% Enable line breaks for Thai text
\XeTeXlinebreaklocale "th"
% \XeTeXlinebreakskip = 0pt plus 2pt minus 1pt

\newfontfamily\thaifonttt{Arundina Sans Mono}
\setmainfont{Sukhumvit Set}
\setsansfont{Prompt}
\setmonofont{Arundina Sans Mono}

% Custom names for contents and chapters
\renewcommand{\contentsname}{สารบัญ}
\renewcommand{\chaptername}{บทที่}

\makeatletter
\renewcommand{\sphinxVerbatimHighlightLine}[1]{\textcolor{red}{#1}}
\fvset{fontsize=\Large}
\renewcommand{\Verbatim}[1][1]{\small\oldVerbatim[#1]}
\makeatother
""",
    "extrapackages": r"""
\usepackage{draftwatermark}
\SetWatermarkText{Piyathon 0.1.1-01}
\SetWatermarkScale{0.3}
\SetWatermarkColor[gray]{0.95}
\SetWatermarkAngle{45}
""",
}
