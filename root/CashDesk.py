from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Worker import Worker
    from Visitor import Visitor


class CashDesk:
    __worker: Optional[Worker]
    __visitorList: List[Visitor]

    def __init__(self) -> None:
        self.__worker = None
        self.__visitorList = list()

    def getWorker(self) -> Worker:
        return self.__worker

    def setWorker(self, value: Worker) -> None:
        self.__worker = value

    def addVisitorToQueue(self, visitor: Visitor) -> None:
        self.__visitorList.append(visitor)

    def getFirstVisitor(self) -> Optional[Visitor]:
        if self.__visitorList:
            return self.__visitorList.pop(0)
        return None

    def getVisitorList(self) -> List[Visitor]:
        return self.__visitorList

    def removeVisitor(self, visitor: Visitor):
        self.__visitorList.remove(visitor)
