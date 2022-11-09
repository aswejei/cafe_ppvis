from __future__ import annotations
from typing import TYPE_CHECKING
import time

if TYPE_CHECKING:
    from extension6.CoffeeHouseWithSupplyManager import CoffeeHouseWithSupplyManager
    from root.Ingredient import Ingredient
    from root.Product import Product


class SupplyManager:
    _model: CoffeeHouseWithSupplyManager
    _state: bool

    def __init__(self, model: CoffeeHouseWithSupplyManager):
        self._model = model
        self._state = True

    def renewIngredient(self, ingredient: Ingredient, amount: int) -> None:
        self._state = False
        print(f'Supply manager {self.__hash__()} left to get missing ingredient(Missing ingredient is {ingredient}) ')
        time.sleep(amount/10)
        self._model.addIngredient(ingredient, amount)
        print(f'Supply manager {self.__hash__()} successfully bought missing ingredient({ingredient}).\nMissing '
              f'ingredient is now renewed')
        self._state = True

    def renewProduct(self, product: Product, amount: int) -> None:
        self._state = False
        print(f'Supply manager {self.__hash__()} left to get missing product(Missing ingredient is {product}) ')
        time.sleep(amount/10)
        self._model.addDessert(product, amount)
        print(f'Supply manager {self.__hash__()} successfully bought missing product({product}).\nMissing '
              f'product is now renewed')
        self._state = True

    def getManagerState(self) -> bool:
        return self._state
