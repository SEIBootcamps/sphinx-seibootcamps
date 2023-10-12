import importlib.metadata
from os import path
from pathlib import Path
from typing import TYPE_CHECKING, Any

from docutils import nodes

from . import bs

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__name__ = "sphinx_seibootcamps"
__version__ = importlib.metadata.version(__name__)

package_dir = Path(path.abspath(path.dirname(__file__)))


def add_preconnect_to_page_context(app, pagename, templatename, context, doctree):
    context["html_preconnect"] = app.config.seibootcamps_html_preconnect


def setup(app: "Sphinx") -> dict[str, Any]:
    # Config values
    app.add_config_value("seibootcamps_html_preconnect", [], rebuild="html")

    # Theme: seibootcamps
    app.add_html_theme("seibootcamps", str((package_dir / "theme").resolve()))
    app.add_css_file("css/styles.css.map")
    app.add_js_file("js/darkmode.js")

    bs.setup(app)
    bs.roles.setup(app)

    # Events
    app.connect("html-page-context", add_preconnect_to_page_context)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
