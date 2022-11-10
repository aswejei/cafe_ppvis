from __future__ import annotations
import random
from typing import TYPE_CHECKING

from python.root.Visitor import Visitor

if TYPE_CHECKING:
    from python.root.CoffeeHouse import CoffeeHouse
    from python.root.Product import Product


class VisitorWithLastChance(Visitor):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def failDesiredProduct(self, currentTime: int, product: Product) -> None:
        if self._successRating == 5:
            self._successRating = 4
            menu = self._model.getMenu()
            self._desiredProduct = menu[random.choice(range(len(menu)))]
        else:
            super().failDesiredProduct(currentTime, product)
