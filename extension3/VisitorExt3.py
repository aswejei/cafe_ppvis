from __future__ import annotations
from typing import TYPE_CHECKING

from root.Visitor import Visitor

if TYPE_CHECKING:
    from root.CoffeeHouse import CoffeeHouse
    from root.Product import Product


class VisitorExt3(Visitor):
    def __init__(self, model: CoffeeHouse):
        super().__init__(model)

    def failDesiredProduct(self, currentTime: int, product: Product) -> None:
        if product.isNeedPrepare():
            self._successRating -= 1
            if self._successRating > 1:
                return None
        super().failDesiredProduct(currentTime, product)
