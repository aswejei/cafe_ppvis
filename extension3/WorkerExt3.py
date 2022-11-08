from __future__ import annotations
import random
from typing import TYPE_CHECKING

from root.Worker import Worker

if TYPE_CHECKING:
    from root.CashDesk import CashDesk
    from root.CoffeeHouse import CoffeeHouse


class WorkerExt3(Worker):
    def __init__(self, model: CoffeeHouse, cashDesk: CashDesk):
        super().__init__(model, cashDesk)

    def _prepareProductProcess(self, currentTime: int) -> None:
        if self._currentRecipe is not None:
            isFail = random.choice([True, False])
            if isFail:
                self._cashDesk.getFirstVisitor().failDesiredProduct(currentTime, self._currentProduct)
                self._prepareProductFinished(currentTime)
        super()._prepareProductProcess(currentTime)
