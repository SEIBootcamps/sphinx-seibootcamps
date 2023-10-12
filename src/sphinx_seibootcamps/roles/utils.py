from typing import TYPE_CHECKING

from docutils import nodes

if TYPE_CHECKING:
    from typing import Callable, List, Optional, Tuple


def get_role_function(node: nodes.Node, opts_fn: "Optional[Callable]") -> "Callable":
    """Generate role function."""

    def role_function(
        _, rt: str, t: str, *__, **___
    ) -> "Tuple[List[nodes.Node], List[nodes.system_message]]":
        # return [nodes.inline(rt, t, classes=_span_roles[role_name])], []
        return [node(rt, t, **opts_fn())], []

    return role_function
