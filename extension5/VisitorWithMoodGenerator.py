from __future__ import annotations
from typing import TYPE_CHECKING

from extension5.VisitorWithMood import VisitorWithMood
from root.VisitorGenerator import VisitorGenerator

if TYPE_CHECKING:
    from root.CoffeeHouse import CoffeeHouse


class VisitorWithMoodGenerator(VisitorGenerator):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def _generateVisitor(self) -> VisitorWithMood:
        return VisitorWithMood(self._model)
