from __future__ import annotations
from typing import TYPE_CHECKING

from extension2.VisitorWithLastChance import VisitorWithLastChance
from root.Visitor import Visitor

if TYPE_CHECKING:
    from root.VisitorGenerator import VisitorGenerator
    from root.CoffeeHouse import CoffeeHouse


class VisitorGeneratorExt2(VisitorGenerator):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def _generateVisitor(self) -> Visitor:
        return VisitorWithLastChance(self._model)
