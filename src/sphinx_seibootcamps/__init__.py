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


def cmd_role(_, rawtext, text, *__, **___):
    """Role for wrapping text in <span class="cmd">."""

    return [nodes.inline(rawtext, text, classes=["cmd"])], []


def setup(app: "Sphinx") -> dict[str, Any]:
    # Theme: seibootcamps
    app.add_html_theme("seibootcamps", str((package_dir / "theme").resolve()))
    app.add_css_file("css/styles.css.map")
    app.add_js_file("js/darkmode.js")

    app.add_role("cmd", cmd_role)

    bs.setup(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
