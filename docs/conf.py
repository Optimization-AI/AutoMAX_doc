# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, '..')
sys.path.insert(0, '../..')

# -- Project information -----------------------------------------------------
project = 'AutoMAX'
copyright = '2024, Optimization-AI Lab'
author = 'Optimization-AI Lab'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.jquery',
    'autodocsumm',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sphinx = False

html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'torch': ('https://pytorch.org/docs/master/', None),
}

add_module_names = False

autodoc_default_options = {
    'autosummary-no-titles': True,
    'autosummary-force-inline': True,
    'autosummary-nosignatures': True,
}
autodoc_default_flags = ['members']

myst_enable_extensions = ['colon_fence', 'deflist']


def setup(app):
    def skip(app, what, name, obj, skip, options):
        members = [
            '__init__',
            '__repr__',
            '__weakref__',
            '__dict__',
            '__module__',
        ]
        return True if name in members else skip

    app.connect('autodoc-skip-member', skip)

    app.add_js_file(None, body="""
        function fetchAndDownload(url, filename) {
        fetch(url)
            .then(res => res.blob())
            .then(blob => {
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = filename;
            a.click();
            URL.revokeObjectURL(a.href);
            })
            .catch(err => console.error('Download failed:', err));
        }
        """)
