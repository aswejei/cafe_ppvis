from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from root.CashDesk import CashDesk
    from root.CoffeeHouse import CoffeeHouse
    from root.Product import Product
    from root.Recipe import Recipe
    from root.RecipeStep import RecipeStep


class Worker:
    _cashDesk: CashDesk
    _model: CoffeeHouse
    _currentProduct: Optional[Product]
    _currentRecipe: Optional[Recipe]
    _recipeStepIndex: int
    _nextActionTime: int

    def __init__(self, model: CoffeeHouse, cashDesk: CashDesk):
        self._currentRecipe = None
        self._currentProduct = None
        self._recipeStepIndex = 0
        self._nextActionTime = 0
        self._model = model
        self._cashDesk = cashDesk

    def process(self, currentTime: int) -> None:
        if self._currentRecipe is None:
            visitor = self._cashDesk.getFirstVisitor()
            if visitor is None:
                return None
            self._currentProduct = visitor.getDesiredProduct()
            if self._currentProduct.isNeedPrepare():
                self._currentRecipe = self._model.getRecipe(self._currentProduct)
                print(f'Time={currentTime} Worker({self.__hash__()}) start prepare product {self._currentProduct}')
            else:
                visitor.askDesiredProduct(currentTime)
        if self._currentRecipe is not None:
            self._prepareProductProcess(currentTime)

    def _prepareProductProcess(self, currentTime: int) -> None:
        if self._nextActionTime == 0:
            self._recipeStepIndex = 0
            step = self.__getRecipeStep()
            assert step is not None

            self._nextActionTime = currentTime
            self._processStepTime(step)
        elif self._nextActionTime <= currentTime:
            step = self.__getRecipeStep()
            assert step is not None
            result = self._model.takeIngredient(step.getIngredient(), step.getAmount())
            if not result:
                self._cashDesk.getFirstVisitor().failDesiredProduct(currentTime, self._currentProduct)
                self._prepareProductFinished(currentTime)
            self._recipeStepIndex += 1
            nextStep = self.__getRecipeStep()
            if nextStep is None:
                # finish prepare
                self._model.takeProduct(self._currentProduct)
                self._cashDesk.getFirstVisitor().givePreparedProduct(currentTime, self._currentProduct)
                self._prepareProductFinished(currentTime)
            else:
                self._processStepTime(nextStep)
                self._prepareProductProcess(currentTime)

    def _prepareProductFinished(self, currentTime: int) -> None:
        print(f'Time={currentTime} Worker({self.__hash__()}) finish prepare {self._currentProduct}')
        self._currentProduct = None
        self._currentRecipe = None
        self._recipeStepIndex = 0
        self._nextActionTime = 0

    def _processStepTime(self, step: RecipeStep):
        self._nextActionTime += step.getTime()

    def __getRecipeStep(self) -> Optional[RecipeStep]:
        assert self._currentRecipe is not None
        stepList = self._currentRecipe.getStepList()
        if len(stepList) > self._recipeStepIndex:
            return stepList[self._recipeStepIndex]
        else:
            return None
