from typing import TYPE_CHECKING

from . import compare, console, admonitions

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    compare.setup(app)
    console.setup(app)
    admonitions.setup(app)
