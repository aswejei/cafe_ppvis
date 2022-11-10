from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from python.root.CoffeeHouse import CoffeeHouse
if TYPE_CHECKING:
    from python.extension6.SupplyManager import SupplyManager
    from python.root.Ingredient import Ingredient
    from python.root.Product import Product


class CoffeeHouseWithSupplyManager(CoffeeHouse):
    _supplyManager: Optional[SupplyManager]

    def __init__(self):
        super().__init__()
        self._supplyManager = None

    def addIngredient(self, ingredient: Ingredient, amount: int) -> None:
        super().addIngredient(ingredient, amount)
        self._supplyManager.addIngredientInitialAmount(ingredient, amount)

    def addDessert(self, dessert: Product, amount: int) -> None:
        super().addDessert(dessert, amount)
        self._supplyManager.addProductInitialAmount(dessert, amount)

    def addSupplyManager(self, supplyManager: SupplyManager) -> None:
        if self._supplyManager is None:
            self._supplyManager = supplyManager

    def takeProduct(self, product: Product) -> None:
        if not product.isNeedPrepare():
            currentAmount = self._dessertMap.get(product, 0)
            if currentAmount > 0:
                self._dessertMap[product] -= 1
                if self._dessertMap[product] < 1:
                    if self._supplyManager.getManagerState():
                        self._supplyManager.renewProduct(product, self.__currentTime)

    def takeIngredient(self, ingredient: Ingredient, amount: int) -> bool:
        currentAmount = self._ingredientMap.get(ingredient, 0)
        if (currentAmount - amount) >= 0:
            self._ingredientMap[ingredient] = currentAmount - amount
            if self._ingredientMap[ingredient] < 0:
                if self._supplyManager.getManagerState():
                    self._supplyManager.renewIngredient(ingredient, currentTime=self.__currentTime)
            return True
        return False
