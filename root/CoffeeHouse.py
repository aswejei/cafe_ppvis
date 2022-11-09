from __future__ import annotations
from typing import Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from root.CashDesk import CashDesk
    from root.Ingredient import Ingredient
    from root.Product import Product
    from root.Recipe import Recipe
    from root.Visitor import Visitor
    from root.VisitorGenerator import VisitorGenerator

from root.VisitorRequestStatus import VisitorRequestStatus
from root.Settings import Settings


class CoffeeHouse:
    __visitorGenerator: Optional[VisitorGenerator]
    _dessertMap: Dict[Product, int]
    __recipeMap: Dict[Product, Recipe]
    __cashDeskList: List[CashDesk]
    __menuList: List[Product]
    __outgoingVisitorList: List[Visitor]
    _ingredientMap: Dict[Ingredient, int]
    __currentTime: int
    __ratingSum: int
    __ratingAmount: int

    def __init__(self):
        self.__visitorGenerator = None
        self._dessertMap = dict()
        self.__recipeMap = dict()
        self.__cashDeskList = list()
        self.__menuList = list()
        self.__outgoingVisitorList = list()
        self._ingredientMap = dict()
        self.__currentTime = 0
        self.__ratingSum = 0
        self.__ratingAmount = 0

    def run(self) -> None:
        self.createMenu()
        while self.__currentTime < Settings.CLOSING_TIME:
            for visitor in self.__outgoingVisitorList:
                visitor.getCashDesk().removeVisitor(visitor)
            self.__outgoingVisitorList.clear()

            assert self.__visitorGenerator is not None
            self.__visitorGenerator.process(self.__currentTime)
            for cash_desk in self.__cashDeskList:
                cash_desk.getWorker().process(self.__currentTime)
                for visitor in cash_desk.getVisitorList():
                    visitor.process(self.__currentTime)
            self.__currentTime += Settings.TICK_TIME

    def requestProduct(self, product: Product) -> VisitorRequestStatus:
        if product.isNeedPrepare():
            if product in self.__recipeMap:
                return VisitorRequestStatus.NEED_PREPARE
        else:
            if self._dessertMap.get(product, 0) > 0:
                return VisitorRequestStatus.SUCCESS
        return VisitorRequestStatus.PRODUCT_MISSING

    def setVisitorGenerator(self, visitorGenerator: VisitorGenerator) -> None:
        self.__visitorGenerator = visitorGenerator

    def addRating(self, rating: int) -> None:
        self.__ratingSum += rating
        self.__ratingAmount += 1

    def getAvgRating(self) -> float:
        return float(self.__ratingSum) / float(self.__ratingAmount)

    def visitorLeave(self, visitor: Visitor) -> None:
        self.__outgoingVisitorList.append(visitor)

    def createMenu(self) -> None:
        self.__menuList += list(self._dessertMap.keys())
        self.__menuList += list(self.__recipeMap.keys())

    def getMenu(self) -> List[Product]:
        return self.__menuList

    def addDessert(self, dessert: Product, amount: int) -> None:
        self._dessertMap[dessert] = amount

    def takeProduct(self, product: Product) -> None:
        if not product.isNeedPrepare():
            currentAmount = self._dessertMap.get(product, 0)
            if currentAmount > 0:
                self._dessertMap[product] -= 1

    def addRecipe(self, product: Product, recipe: Recipe) -> None:
        self.__recipeMap[product] = recipe

    def getRecipe(self, product: Product) -> Optional[Recipe]:
        return self.__recipeMap.get(product, None)

    def addIngredient(self, ingredient: Ingredient, amount: int) -> None:
        self._ingredientMap[ingredient] = amount

    def takeIngredient(self, ingredient: Ingredient, amount: int) -> bool:
        currentAmount = self._ingredientMap.get(ingredient, 0)
        if (currentAmount - amount) >= 0:
            self._ingredientMap[ingredient] = currentAmount - amount
            return True
        return False

    def addCashDesk(self, cashDesk: CashDesk) -> None:
        self.__cashDeskList.append(cashDesk)

    def getCashDeskList(self) -> List[CashDesk]:
        return self.__cashDeskList
