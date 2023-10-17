from typing import TYPE_CHECKING, Any
import importlib.metadata
from os import path
from pathlib import Path
from sphinx.util.osutil import copyfile

from . import bs, compare, console

if TYPE_CHECKING:
    from typing import Any, Dict

    from sphinx.application import Sphinx

__name__ = "sphinx_seibootcamps"
__version__ = importlib.metadata.version(__name__)

package_dir = Path(path.abspath(path.dirname(__file__)))
theme_dir = package_dir / "theme"


def add_preconnect_to_page_context(app, _, __, context, ___) -> None:
    context["html_preconnect"] = app.config.seibootcamps_html_preconnect


def copy_seibootcamps_assets(app: "Sphinx", exc: Exception) -> None:
    staticdir = (Path(app.builder.outdir) / "_static").resolve()
    assets = [
        "css/styles.css",
        "css/styles.css.map",
        "js/darkmode.js",
    ]
    for f in assets:
        source = theme_dir / f
        dest = staticdir / "seibootcamps" / Path(f).name
        copyfile(str(source), str(dest))


def setup(app: "Sphinx") -> "Dict[str, Any]":
    # Config values
    app.add_config_value("seibootcamps_html_preconnect", [], rebuild="html")

    # Theme: seibootcamps
    app.add_html_theme("seibootcamps", str((package_dir / "theme").resolve()))
    app.add_css_file("seibootcamps/styles.css")
    app.add_css_file("seibootcamps/styles.css.map")
    app.add_js_file(  # Bootstrap JS
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
        loading_method="defer",
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
        crossorigin="anonymous",
    )
    app.add_js_file("seibootcamps/darkmode.js")

    bs.setup(app)
    compare.setup(app)
    console.setup(app)

    # Events
    app.connect("html-page-context", add_preconnect_to_page_context)
    app.connect("build-finished", copy_seibootcamps_assets)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
