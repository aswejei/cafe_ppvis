from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from root.KitchenMachine import KitchenMachine
    from root.Ingredient import Ingredient


class RecipeStep:
    __ingredient: Ingredient
    __amount: int
    __machine: Optional[KitchenMachine]
    __time: int

    def __init__(self, ingredient: Ingredient, amount: int, machine: Optional[KitchenMachine], time: int):
        self.__ingredient = ingredient
        self.__time = time
        self.__amount = amount
        self.__machine = machine

    def getIngredient(self) -> Ingredient:
        return self.__ingredient

    def getTime(self) -> int:
        return self.__time

    def getAmount(self) -> int:
        return self.__amount

    def getMachine(self) -> KitchenMachine:
        return self.__machine
