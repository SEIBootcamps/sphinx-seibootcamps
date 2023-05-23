"""sphinx_seibootcamps.bs

Bootstrap-specific extensions.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from . import toctree


def setup(app: "Sphinx") -> None:
    toctree.setup(app)
