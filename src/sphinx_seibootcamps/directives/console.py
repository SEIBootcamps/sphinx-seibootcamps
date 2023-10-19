from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst.directives.body import ParsedLiteral

from ..roles.utils import get_role_function

if TYPE_CHECKING:
    from typing import List

    from sphinx.application import Sphinx


class Console(ParsedLiteral):
    def run(self) -> "List[nodes.Node]":
        node, *rest = super().run()
        node["classes"] += ["console"]
        return [node] + rest


def setup(app: "Sphinx") -> None:
    app.add_directive("console", Console)
    app.add_role(
        "cmd", get_role_function(nodes.inline, opts_fn=lambda: {"classes": ["cmd"]})
    )
