# -*- coding: utf-8 -*-

import re
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Example Site"
slug = re.sub(r"\W+", "-", project.lower())
copyright = "2021, TotalDebug"
author = "TotalDebug"

# The short X.Y version
version = "2.0"
# The full version, including alpha/beta/rc tags
release = ""

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "sphinxcontrib.napoleon",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
source_suffix = ".rst"

master_doc = "index"
language = "en"
gettext_compact = False

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "default"


html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": True,
    "navigation_depth": 5,
}

htmlhelp_basename = slug


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    ("index", "{0}.tex".format(slug), project, author, "manual"),
]


man_pages = [("index", slug, project, [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        author,
        "TotalDebug",
        "",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------
