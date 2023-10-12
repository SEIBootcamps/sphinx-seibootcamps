from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes

if TYPE_CHECKING:
    from typing import List

    from sphinx.application import Sphinx


class Compare(Directive):
    has_content = True
    option_spec = {"class": directives.class_option}

    def run(self) -> "List[nodes.Element]":
        set_classes(self.options)
        text = "\n".join(self.content)
        container_node = nodes.container(text, **self.options)
        container_node["classes"] += ["compare"]
        self.state.nested_parse(self.content, self.content_offset, container_node)
        return [container_node]


def setup(app: "Sphinx") -> None:
    app.add_directive("compare", Compare)
