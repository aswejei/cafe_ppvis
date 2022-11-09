from typing import Optional

from extension6.SupplyManagerWorkPlace import SupplyManagerWorkPlace
from root.CoffeeHouse import CoffeeHouse
from root.Ingredient import Ingredient
from root.Product import Product


class CoffeeHouseWithSupplyManager(CoffeeHouse):
    _supplyManagerWorkPlace: Optional[SupplyManagerWorkPlace]

    def __init__(self):
        super().__init__()
        self._supplyManagerWorkPlace = None

    def addIngredient(self, ingredient: Ingredient, amount: int) -> None:
        super().addIngredient(ingredient, amount)
        self._supplyManagerWorkPlace.addIngredientInitialAmount(ingredient, amount)

    def addDessert(self, dessert: Product, amount: int) -> None:
        super().addDessert(dessert, amount)
        self._supplyManagerWorkPlace.addProductInitialAmount(dessert, amount)

    def addSupplyManagerWorkPlace(self, supplyManagerWorkPlace: SupplyManagerWorkPlace) -> None:
        if self._supplyManagerWorkPlace is None:
            self._supplyManagerWorkPlace = supplyManagerWorkPlace

    def takeProduct(self, product: Product) -> None:
        if not product.isNeedPrepare():
            currentAmount = self._dessertMap.get(product, 0)
            if currentAmount > 0:
                self._dessertMap[product] -= 1
                if self._dessertMap[product] < 1:
                    self._supplyManagerWorkPlace.requestProductRenew(product)

    def takeIngredient(self, ingredient: Ingredient, amount: int) -> bool:
        currentAmount = self._ingredientMap.get(ingredient, 0)
        if (currentAmount - amount) >= 0:
            self._ingredientMap[ingredient] = currentAmount - amount
            if self._ingredientMap[ingredient] < 0:
                self._supplyManagerWorkPlace.requestIngredientRenew(ingredient)
            return True
        return False
