from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def reduce(self, bank, to: str):
        pass

    @abstractmethod
    def plus(self, addend):
        pass

    @abstractmethod
    def times(self, multiplier: int):
        pass