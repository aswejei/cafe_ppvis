from __future__ import annotations
import random
from typing import TYPE_CHECKING

from root.Visitor import Visitor
if TYPE_CHECKING:
    from root.CoffeeHouse import CoffeeHouse

class VisitorWithMood(Visitor):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)
        self.__ifWantsToLeave()

    def __ifWantsToLeave(self) -> None:
        mood = random.choice(range(10))
        if mood < 3:
            self._cashDesk.removeVisitor(self)

