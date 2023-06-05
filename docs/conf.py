# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys

print(sys.executable)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "ACCESS-NRI Intake catalog"
copyright = "2023, ACCESS-NRI"
author = "ACCESS-NRI"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    #    "IPython.sphinxext.ipython_console_highlighting",
    "numpydoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "myst_nb",
    "sphinx_panels",
    "sphinx_copybutton",
]

# Don't load the bootstrap 4 CSS classes relevant to panels
panels_add_bootstrap_css = False

autosummary_generate = True
autodoc_typehints = "none"
autodoc_member_order = "groupwise"

# Config numpydoc
numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = False
numpydoc_class_members_toctree = False

# autoapi directives
# autoapi_dirs = ["../src/access_nri_intake"]
# autoapi_add_toctree_entry = False
# autoapi_ignore = ["**.ipynb_checkpoints"]
# autoapi_python_class_content = "class"
# autoapi_options = [
#     "members",
#     "inherited-members",
#     "show-inheritance",
#     "show-module-summary",
# ]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The master toctree document.
master_doc = "index"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Config myst-nb
nb_execution_excludepatterns = [
    "tutorial.ipynb",
    "building_intake-esm_catalogs.ipynb",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_context = {
    "github_user": "dougiesquire",
    "github_repo": "access-nri-intake-catalog",
    "github_version": "main",
    "doc_path": "./docs",
}
html_theme_options = {
    "use_edit_page_button": True,
    "github_url": "https://github.com/ACCESS-NRI/access-nri-intake-catalog",
    "logo": {
        "image_light": "_static/accessnri_light.png",
        "image_dark": "_static/accessnri_dark.png",
    },
}
