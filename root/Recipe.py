from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from root.RecipeStep import RecipeStep


class Recipe:
    __stepList: List[RecipeStep]

    def __init__(self):
        self.__stepList = list()

    def addStep(self, step: RecipeStep) -> Recipe:
        self.__stepList.append(step)
        return self

    def getStepList(self) -> List[RecipeStep]:
        return self.__stepList
