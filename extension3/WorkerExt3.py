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
                self._prepareProductFinished(currentTime)
                if self._cashDesk.getFirstVisitor() in None:
                    return None
                self._cashDesk.getFirstVisitor().failDesiredProduct(currentTime, self._currentProduct)
                return None
        super()._prepareProductProcess(currentTime)
