from typing import TYPE_CHECKING, Any
import importlib.metadata
from os import path
from pathlib import Path
from sphinx.util.osutil import copyfile, ensuredir

from . import bs, directives

if TYPE_CHECKING:
    from typing import Any, Dict

    from sphinx.application import Sphinx
    from sphinx.config import Config

__name__ = "sphinx_seibootcamps"
__version__ = importlib.metadata.version(__name__)

package_dir = Path(path.abspath(path.dirname(__file__)))
themes_dir = package_dir / "themes"
seibootcamps_theme_dir = themes_dir / "seibootcamps"
theme_static_assets = ["darkmode.js"]


def setup(app: "Sphinx") -> "Dict[str, Any]":
    # Config values
    app.add_config_value("seibootcamps_html_preconnect", [], rebuild="html")

    # Theme: seibootcamps
    app.add_html_theme("seibootcamps", str(seibootcamps_theme_dir.resolve()))
    app.connect("config-inited", add_theme_static_files)
    app.connect("build-finished", copy_theme_static_files)
    app.connect("html-page-context", add_preconnect_to_page_context)

    # Setup Bootstrap roles, CSS, and other stuff
    bs.setup(app)
    # Directives
    directives.setup(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_preconnect_to_page_context(app, _, __, context, ___) -> None:
    context["html_preconnect"] = app.config.seibootcamps_html_preconnect


def add_theme_static_files(app: "Sphinx", config: "Config") -> None:
    # only run this if the theme is seibootcamps
    if config.html_theme == "seibootcamps":
        for f in theme_static_assets:
            app.add_js_file(f)


def copy_theme_static_files(app: "Sphinx", _) -> None:
    # only run this if the theme is seibootcamps
    if app.config.html_theme == "seibootcamps":
        out_static_dir = (Path(app.builder.outdir) / "_static").resolve()
        source_static_dir = seibootcamps_theme_dir / "static"
        for f in theme_static_assets:
            source = source_static_dir / f
            dest = out_static_dir / f
            ensuredir(str(dest.parent))
            copyfile(str(source), str(dest))
