from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from python.root.CoffeeHouse import CoffeeHouse
from python.root.Settings import Settings

if TYPE_CHECKING:
    from python.extension6.SupplyManager import SupplyManager
    from python.root.Ingredient import Ingredient
    from python.root.Product import Product


class CoffeeHouseWithSupplyManager(CoffeeHouse):
    _supplyManager: Optional[SupplyManager]

    def __init__(self):
        super().__init__()
        self._supplyManager = None

    def run(self) -> None:
        self.createMenu()
        while self._currentTime < Settings.CLOSING_TIME:
            for visitor in self.__outgoingVisitorList:
                visitor.getCashDesk().removeVisitor(visitor)
            self.__outgoingVisitorList.clear()
            assert self.__visitorGenerator is not None
            self.__visitorGenerator.process(self._currentTime)
            for cash_desk in self.__cashDeskList:
                cash_desk.getWorker().process(self._currentTime)
                for visitor in cash_desk.getVisitorList():
                    visitor.process(self._currentTime)
            self._supplyManager.process(self._get_missing_products(), self._currentTime)
            self._currentTime += Settings.TICK_TIME

    def addIngredient(self, ingredient: Ingredient, amount: int) -> None:
        super().addIngredient(ingredient, amount)
        self._supplyManager.addIngredientInitialAmount(ingredient, amount)

    def addDessert(self, dessert: Product, amount: int) -> None:
        super().addDessert(dessert, amount)
        self._supplyManager.addProductInitialAmount(dessert, amount)

    def addSupplyManager(self, supplyManager: SupplyManager) -> None:
        if self._supplyManager is None:
            self._supplyManager = supplyManager

    def _get_missing_products(self):
        buy_list = list()
        for dessert in self._dessertMap:
            if self._dessertMap[dessert] <= 0:
                buy_list.append(dessert)
        for ingredient in self._ingredientMap:
            if self._ingredientMap[ingredient] <= 0:
                buy_list.append(ingredient)
        return buy_list