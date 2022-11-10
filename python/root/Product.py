class Product:
    __name: str
    __isNeedPrepare: bool

    def __init__(self, name: str, isNeedPrepare: bool):
        self.__name = name
        self.__isNeedPrepare = isNeedPrepare

    def getName(self) -> str:
        return self.__name

    def isNeedPrepare(self) -> bool:
        return self.__isNeedPrepare

    def __repr__(self) -> str:
        return f'Product({self.__hash__()}), name: {self.__name}'
