from __future__ import annotations
from typing import TYPE_CHECKING
from extension3.VisitorExt3 import VisitorExt3
from root.VisitorGenerator import VisitorGenerator

if TYPE_CHECKING:
    from root.CoffeeHouse import CoffeeHouse


class VisitorGeneratorExt3(VisitorGenerator):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def _generateVisitor(self) -> VisitorExt3:
        return VisitorExt3(self._model)
