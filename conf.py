# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
import json
import os
from pathlib import Path
import logging

# sys.path.insert(0, os.path.abspath('../'))
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# Use footnote size for code block.
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"


PygmentsBridge.latex_formatter = CustomLatexFormatter

# ##################### pre process ###########################


root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, ".math.json")) as f:
    meta_data = json.load(f)
    rst_exclude = meta_data["rst_exclude"]
    md_include = meta_data["md_include"]

clean_dir = set(os.listdir(root)) - {'.git', '.gitignore', '_build', '_static', 'mx-theme'}

clean_dir = [os.path.join(root, d) for d in clean_dir]

logging.getLogger().setLevel(logging.INFO)


def clean_rst():
    logging.info("clean .rst")
    _rst_exclude = set(rst_exclude)
    for _clean_dir in clean_dir:
        for _root, dirs, files in os.walk(_clean_dir):
            for fn in files:
                if '.rst' in fn:
                    filename = os.path.join(_root, fn)
                    if filename in rst_exclude:
                        continue
                    logging.info("remove %s" % filename)
                    os.remove(filename)


def generate_rst():
    logging.info("converting .md with math expression to .rst")
    _md_include = set([str(Path(os.path.join(root, fn))) for fn in md_include])
    for _clean_dir in clean_dir:
        for _root, dirs, files in os.walk(_clean_dir):
            for fn in files:
                if '.md' in fn:
                    src = Path(os.path.join(_clean_dir, fn))
                    if str(src) not in _md_include:
                        continue
                    tar = src.with_suffix(".rst")
                    logging.info("%s -> %s" % (src, tar))
                    os.system("pandoc %s -t rst > %s" % (src, tar))


logging.info("#" * 30)
clean_rst()
generate_rst()
logging.info("#" * 30)

################################################################

# -- Project information -----------------------------------------------------

project = 'Handbook for Data Science and Artificial Intelligence'
copyright = '2019, tongshiwei'
author = 'tongshiwei'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    # 'sphinx_gallery.gen_gallery',
    'nbsphinx',
    # 'IPython.sphinxext.ipython_console_highlighting',
    # 'IPython.sphinxext.ipython_directive',
    # 'm2r',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {'.md': CommonMarkParser}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'mx-theme', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


html_theme_path = ['mx-theme']
html_theme = 'mxtheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links': [
        # ('伯克利深度学习课程', 'https://courses.d2l.ai/berkeley-stat-157/index.html', True, 'fas fa-user-graduate'),
        # ('PDF', 'https://zh.d2l.ai/d2l-zh.pdf', True, 'fas fa-file-pdf'),
        # ('Jupyter 记事本文件', 'https://zh.d2l.ai/d2l-zh.zip', True, 'fas fa-download'),
        # ('讨论', 'https://discuss.gluon.ai/c/lecture?order=views', True, 'fab fa-discourse'),
        ('GitHub', 'https://github.com/tswsxk', True, 'fab fa-github'),
        ('CodeBook', 'https://github.com/tswsxk/CodeBook', True, 'fas fa-book'),
        ('HomePage', 'https://tswsxk.github.io', True, 'fas fa-home'),
    ],
    'show_footer': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'HB4DSAI'

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

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'handbook.tex', 'HandBook Documentation',
     'tongshiwei', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'longling', 'longling Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'longling', 'longling Documentation',
     author, 'longling', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    app.add_transform(AutoStructify)
    app.add_config_value('recommonmark_config', {
    }, True)
    app.add_javascript('google_analytics.js')
    app.add_javascript('discuss.js')
    # app.connect('source-read', image_caption)
