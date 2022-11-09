import time

from root.CoffeeHouse import CoffeeHouse
from root.Ingredient import Ingredient
from root.Product import Product


class SupplyManager:
    _model: CoffeeHouse
    _state: bool

    def __init__(self, model: CoffeeHouse):
        self._model = model
        self._state = True

    def renewIngredient(self, ingredient: Ingredient, amount: int) -> None:
        self._state = False
        time.sleep(amount/10)
        self._model.addIngredient(ingredient, amount)

    def renewProduct(self, product: Product, amount: int) -> None:
        self._state = False
        time.sleep(amount/10)
        self._model.addDessert(product, amount)

    def getManagerState(self) -> bool:
        return self._state
