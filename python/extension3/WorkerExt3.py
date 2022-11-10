from __future__ import annotations
import random
from typing import TYPE_CHECKING

from python.root.Worker import Worker

if TYPE_CHECKING:
    from python.root.CashDesk import CashDesk
    from python.root.CoffeeHouse import CoffeeHouse


class WorkerExt3(Worker):
    def __init__(self, model: CoffeeHouse, cashDesk: CashDesk):
        super().__init__(model, cashDesk)

    def _prepareProductProcess(self, currentTime: int) -> None:
        if self._currentRecipe is not None:
            isFail = random.choice([True, False])
            if isFail:
                if self._cashDesk.getFirstVisitor() is None:
                    return None
                self._cashDesk.getFirstVisitor().failDesiredProduct(currentTime, self._currentProduct)
                self._prepareProductFinished(currentTime)
                return None
        super()._prepareProductProcess(currentTime)
