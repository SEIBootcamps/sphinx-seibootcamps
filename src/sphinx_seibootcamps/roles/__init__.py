"""sphinx_seibootcamps.roles"""

from typing import TYPE_CHECKING

from docutils import nodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    # Alias title reference to `t` so it can be used in MyST docs to wrap
    # text in <cite></cite> tags.
    app.add_generic_role("t", nodes.title_reference)
