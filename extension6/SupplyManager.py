from __future__ import annotations
from typing import TYPE_CHECKING, Dict
import time

if TYPE_CHECKING:
    from extension6.CoffeeHouseWithSupplyManager import CoffeeHouseWithSupplyManager
    from root.Ingredient import Ingredient
    from root.Product import Product


class SupplyManager:
    _model: CoffeeHouseWithSupplyManager
    _state: bool
    _ingredientInitialAmountMap: Dict[Ingredient, int]
    _productInitialAmountMap: Dict[Product, int]

    def __init__(self, model: CoffeeHouseWithSupplyManager):
        self._model = model
        self._state = True
        self._ingredientInitialAmountMap = dict()
        self._productInitialAmountMap = dict()

    def renewIngredient(self, ingredient: Ingredient) -> None:
        self._state = False
        print(f'Supply manager {self.__hash__()} left to get missing ingredient(Missing ingredient is {ingredient}) ')
        time.sleep(self._ingredientInitialAmountMap[ingredient]/10)
        self._model.addIngredient(ingredient, self._ingredientInitialAmountMap[ingredient])
        print(f'Supply manager {self.__hash__()} successfully bought missing ingredient({ingredient}).\nMissing '
              f'ingredient is now renewed')
        self._state = True

    def renewProduct(self, product: Product) -> None:
        self._state = False
        print(f'Supply manager {self.__hash__()} left to get missing product(Missing ingredient is {product}) ')
        time.sleep(self._productInitialAmountMap[product]/10)
        self._model.addDessert(product, self._productInitialAmountMap[product])
        print(f'Supply manager {self.__hash__()} successfully bought missing product({product}).\nMissing '
              f'product is now renewed')
        self._state = True

    def getManagerState(self) -> bool:
        return self._state

    def addIngredientInitialAmount(self, ingredient: Ingredient, amount: int) -> None:
        if ingredient not in self._ingredientInitialAmountMap:
            self._ingredientInitialAmountMap[ingredient] = amount

    def addProductInitialAmount(self, product: Product, amount: int) -> None:
        if product not in self._productInitialAmountMap:
            self._productInitialAmountMap[product] = amount
