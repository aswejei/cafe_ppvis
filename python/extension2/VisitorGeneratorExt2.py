from __future__ import annotations
from typing import TYPE_CHECKING

from python.extension2.VisitorWithLastChance import VisitorWithLastChance
from python.root.Visitor import Visitor
from python.root.VisitorGenerator import VisitorGenerator
if TYPE_CHECKING:
    from python.root.CoffeeHouse import CoffeeHouse


class VisitorGeneratorExt2(VisitorGenerator):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def _generateVisitor(self) -> Visitor:
        return VisitorWithLastChance(self._model)
