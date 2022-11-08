from __future__ import annotations
from typing import TYPE_CHECKING
from root.Settings import Settings
from root.Visitor import Visitor

if TYPE_CHECKING:
    from root.CoffeeHouse import CoffeeHouse


class VisitorGenerator:
    _model: CoffeeHouse
    __nextActionTime: int

    def __init__(self, model: CoffeeHouse) -> None:
        self.__nextActionTime = 0
        self._model = model

    def process(self, currentTime: int) -> None:
        if self.__nextActionTime <= currentTime:
            visitor = self._generateVisitor()
            self.__nextActionTime += Settings.VISITOR_GENERATE_TIME_PERIOD
            print(f'Time={currentTime} Generate visitor {visitor}')

    def _generateVisitor(self) -> Visitor:
        return Visitor(self._model)
