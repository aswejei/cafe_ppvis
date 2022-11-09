class Ingredient:
    __name: str

    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def __repr__(self):
        return f'Ingredient {self.__hash__()} name:{self.__name}'