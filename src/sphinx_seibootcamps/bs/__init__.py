"""sphinx_seibootcamps.bs

Bootstrap-specific stuff.
"""

from typing import TYPE_CHECKING

from docutils import nodes

from . import icons, roles, toctree
from .betternodes import depart_table, visit_table

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    roles.add_color_roles(app)
    app.connect("html-page-context", toctree.add_toc_to_context)
    app.connect("config-inited", icons.add_icon_substitutions)
    app.add_node(nodes.table, html=(visit_table, depart_table), override=True)
