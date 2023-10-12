from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes

from ..roles.utils import get_role_function

if TYPE_CHECKING:
    from typing import List

    from sphinx.application import Sphinx


class Console(Directive):
    has_content = True
    option_spec = {"class": directives.class_option}

    def run(self) -> "List[nodes.Element]":
        set_classes(self.options)
        text = "\n".join(self.content)
        container_node = nodes.literal_block(text, **self.options)
        container_node["classes"] += ["console"]
        self.state.nested_parse(self.content, self.content_offset, container_node)
        return [container_node]


def setup(app: "Sphinx") -> None:
    app.add_directive("console", Console)
    app.add_role(
        "cmd", get_role_function(nodes.inline, opts_fn=lambda: {"classes": ["cmd"]})
    )
