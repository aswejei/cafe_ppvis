from __future__ import annotations
import random
from typing import TYPE_CHECKING

from python.root.Worker import Worker
if TYPE_CHECKING:
    from python.root.CashDesk import CashDesk
    from python.root.CoffeeHouse import CoffeeHouse
    from python.root.RecipeStep import RecipeStep


class WorkerWithSpeed(Worker):
    __speed: float

    def __init__(self, model: CoffeeHouse, cashDesk: CashDesk):
        super().__init__(model, cashDesk)
        self.__speed = random.choice(range(11))

    def _processStepTime(self, step: RecipeStep) -> None:
        self._nextActionTime += step.getTime() / self.__speed
