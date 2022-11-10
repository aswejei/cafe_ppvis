from __future__ import annotations
import random
from typing import TYPE_CHECKING

from python.root.Visitor import Visitor

if TYPE_CHECKING:
    from python.root.CoffeeHouse import CoffeeHouse


class VisitorWithMood(Visitor):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)
        if self._ifWantsToLeave():
            self._leaveQueue()

    def process(self, currentTime: int) -> None:
        if self._ifWantsToLeave():
            self._leaveQueue()
        else:
            super().process(currentTime)

    def _ifWantsToLeave(self) -> bool:
        mood = random.choice(range(10))
        if mood < 3:
            return True
        return False

    def _leaveQueue(self) -> None:
        self._model.addRating(3)
        self._cashDesk.removeVisitor(self)

