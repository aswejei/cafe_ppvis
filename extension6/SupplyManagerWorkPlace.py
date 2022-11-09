from __future__ import annotations
from typing import List, Dict, TYPE_CHECKING

from extension6.SupplyManager import SupplyManager
from root.Ingredient import Ingredient
from root.Product import Product


class SupplyManagerWorkPlace:
    _supplyManagersList: List[SupplyManager]
    __ingredientInitialAmountMap: Dict[Ingredient, int]
    __productInitialAmountMap: Dict[Product, int]

    def __init__(self):
        self._supplyManagersList = list()
        self.__ingredientInitialAmountMap = dict()
        self.__productInitialAmountMap = dict()

    def addIngredientInitialAmount(self, ingredient: Ingredient, amount: int):
        if ingredient not in self.__ingredientInitialAmountMap:
            self.__ingredientInitialAmountMap[ingredient] = amount

    def addProductInitialAmount(self, product: Product, amount: int):
        if product not in self.__productInitialAmountMap:
            self.__productInitialAmountMap[product] = amount

    def requestIngredientRenew(self, ingredient):
        for manager in self._supplyManagersList:
            if manager.getManagerState():
                manager.renewIngredient(ingredient, self.__ingredientInitialAmountMap[ingredient])

    def requestProductRenew(self, product):
        for manager in self._supplyManagersList:
            if manager.getManagerState():
                manager.renewProduct(product, self.__productInitialAmountMap[product])

    def addSupplyManager(self, manager: SupplyManager):
        assert manager not in self._supplyManagersList
        self._supplyManagersList.append(manager)
