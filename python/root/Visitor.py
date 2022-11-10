from __future__ import annotations
from typing import TYPE_CHECKING
import random

from python.root.Settings import Settings
from python.root.VisitorRequestStatus import VisitorRequestStatus

if TYPE_CHECKING:
    from python.root.Product import Product
    from python.root.CoffeeHouse import CoffeeHouse
    from python.root.CashDesk import CashDesk


class Visitor:
    _model: CoffeeHouse
    _cashDesk: CashDesk
    _desiredProduct: Product
    _nextActionTime: int
    _successRating: int

    def __init__(self, model: CoffeeHouse) -> None:
        self._nextActionTime = 0
        self._successRating = 5
        self._model = model
        menu = model.getMenu()
        self._desiredProduct = menu[random.choice(range(len(menu)))]
        cashDeskList = model.getCashDeskList()
        self._cashDesk = random.choice(cashDeskList)
        self._cashDesk.addVisitorToQueue(self)

    def process(self, currentTime: int) -> None:
        if self._nextActionTime == 0:
            self._nextActionTime = currentTime + Settings.VISITOR_WAITING_TIME
        if currentTime >= self._nextActionTime:
            self._model.addRating(0)
            self._model.visitorLeave(self)
            print(f'Time={currentTime} Visitor leave by timeout {self}')

    def askDesiredProduct(self, currentTime: int) -> None:
        requestStatus = self._model.requestProduct(self._desiredProduct)
        if requestStatus == VisitorRequestStatus.SUCCESS:
            self._model.takeProduct(self._desiredProduct)
            self._model.addRating(self._successRating)
            self._model.visitorLeave(self)
            print(f'Time={currentTime} Visitor({self.__hash__()}) leave with product {self._desiredProduct}')
        elif requestStatus == VisitorRequestStatus.PRODUCT_MISSING:
            self.failDesiredProduct(currentTime, self._desiredProduct)

    def givePreparedProduct(self, currentTime: int, product: Product) -> None:
        self._model.addRating(self._successRating)
        self._model.visitorLeave(self)
        print(f'Time= {currentTime} Visitor({self.__hash__()}) leave with product {product}')

    def failDesiredProduct(self, currentTime: int, product: Product) -> None:
        self._model.addRating(1)
        self._model.visitorLeave(self)
        print(f'Time= {currentTime} Visitor({self.__hash__()}) leave without product {product}')

    def getDesiredProduct(self) -> Product:
        return self._desiredProduct

    def getCashDesk(self) -> CashDesk:
        return self._cashDesk

    def __str__(self) -> str:
        if self in self._cashDesk.getVisitorList():
            return f'Visitor({self.__hash__()})\
             desiredProduct=[{self._desiredProduct}]\
              queuePos={self._cashDesk.getVisitorList().index(self)}'
        else:
            return f'Visitor({self.__hash__()})\
                         desiredProduct=[{self._desiredProduct}]\
                          queuePos: this visitor changed his mood and left the queue'