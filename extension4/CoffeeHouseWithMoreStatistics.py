from __future__ import annotations
from typing import TYPE_CHECKING

from root.CoffeeHouse import CoffeeHouse

if TYPE_CHECKING:
    from root.Product import Product
    from root.Visitor import Visitor


class CoffeeHouseWithMoreStatistics(CoffeeHouse):
    __visitorCounter: int
    __dessertCounter: int
    __drinkCounter: int

    def __init__(self):
        super().__init__()
        self.__visitorCounter = 0
        self.__dessertCounter = 0
        self.__drinkCounter = 0

    def printMoreStatistics(self):
        print(f'Visitors {self.__visitorCounter}')
        print(f'Dessert {self.__dessertCounter}')
        print(f'Drink {self.__drinkCounter}')

    def visitorLeave(self, visitor: Visitor) -> None:
        super().visitorLeave(visitor)
        self.__visitorCounter += 1

    def takeProduct(self, product: Product) -> None:
        super().takeProduct(product)
        if product.isNeedPrepare():
            self.__drinkCounter += 1
        else:
            self.__dessertCounter += 1
