from typing import TYPE_CHECKING

from docutils import nodes

if TYPE_CHECKING:
    from typing import Any, Callable, List, Tuple

    from sphinx.application import Sphinx

_span_roles = {
    "cmd": ["cmd"],
    "blue": ["text-blue"],
    "blue-light": ["text-blue-light"],
    "blue-dark": ["text-blue-dark"],
    "indigo": ["text-indigo"],
    "indigo-light": ["text-indigo-light"],
    "indigo-dark": ["text-indigo-dark"],
    "purple": ["text-purple"],
    "purple-light": ["text-purple-light"],
    "purple-dark": ["text-purple-dark"],
    "pink": ["text-pink"],
    "pink-light": ["text-pink-light"],
    "pink-dark": ["text-pink-dark"],
    "red": ["text-red"],
    "red-light": ["text-red-light"],
    "red-dark": ["text-red-dark"],
    "orange": ["text-orange"],
    "orange-light": ["text-orange-light"],
    "orange-dark": ["text-orange-dark"],
    "yellow": ["text-yellow"],
    "yellow-light": ["text-yellow-light"],
    "yellow-dark": ["text-yellow-dark"],
    "green": ["text-green"],
    "green-light": ["text-green-light"],
    "green-dark": ["text-green-dark"],
    "teal": ["text-teal"],
    "teal-light": ["text-teal-light"],
    "teal-dark": ["text-teal-dark"],
    "cyan": ["text-cyan"],
    "cyan-light": ["text-cyan-light"],
    "cyan-dark": ["text-cyan-dark"],
}


def get_role_function(role_name: str) -> "Callable":
    """Generate role function that wraps text in <span> and adds classes from _span_roles."""

    def role_function(
        _, rt: str, t: str, *__, **___
    ) -> "Tuple[List[nodes.Node], List[nodes.system_message]]":
        return [nodes.inline(rt, t, classes=_span_roles[role_name])], []

    return role_function


def setup(app: "Sphinx") -> dict[str, "Any"]:
    # Alias title reference to `t` so it can be used in MyST docs to wrap
    # text in <cite></cite> tags.
    app.add_generic_role("t", nodes.title_reference)
    for role_name in _span_roles:
        app.add_role(role_name, get_role_function(role_name))
