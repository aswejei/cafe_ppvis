from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, List
import time

if TYPE_CHECKING:
    from python.extension6.CoffeeHouseWithSupplyManager import CoffeeHouseWithSupplyManager
    from python.root.Ingredient import Ingredient
    from python.root.Product import Product


class SupplyManager:
    _model: CoffeeHouseWithSupplyManager
    _state: bool
    _ingredientInitialAmountMap: Dict[Ingredient, int]
    _productInitialAmountMap: Dict[Product, int]
    _buyList: List[Union[Ingredient, Product]]
    _comeBackTime: Union[int, None]

    def __init__(self, model: CoffeeHouseWithSupplyManager):
        self._model = model
        self._ingredientInitialAmountMap = dict()
        self._productInitialAmountMap = dict()
        self._buyList = list()
        self._comeBackTime = None

    def process(self, buyList: List[Union[Ingredient, Product]], currentTime: int) -> None:
        if self._comeBackTime is None:
            if len(buyList) > 0:
                print(f'There is a lack of those products:{buyList}')
                self._buyList = buyList
                self._renewSupplyLeave(currentTime)
        else:
            if currentTime >= self._comeBackTime:
                self._renewSupplyFinish()

    def _renewSupplyLeave(self, currentTime: int) -> None:
        self._comeBackTime = currentTime
        print(f'Supply Manager was informed about lack of products')
        for elem in self._buyList:
            if elem is Ingredient:
                self._comeBackTime += self._ingredientInitialAmountMap[elem] / 10
            elif elem is Product:
                self._comeBackTime += self._productInitialAmountMap[elem] / 10
        print(f'Supply Manager left for {self._comeBackTime - currentTime} to renew products')

    def _renewSupplyFinish(self) -> None:
        for elem in self._buyList:
            if elem is Ingredient:
                self._model.addIngredient(elem, self._ingredientInitialAmountMap[elem])
            elif elem is Product:
                self._model.addDessert(elem, self._productInitialAmountMap[elem])
        print(f'All the products requested previously were restored')
        self._comeBackTime = None

    def getManagerState(self) -> bool:
        return self._state

    def addIngredientInitialAmount(self, ingredient: Ingredient, amount: int) -> None:
        if ingredient not in self._ingredientInitialAmountMap:
            self._ingredientInitialAmountMap[ingredient] = amount

    def addProductInitialAmount(self, product: Product, amount: int) -> None:
        if product not in self._productInitialAmountMap:
            self._productInitialAmountMap[product] = amount
