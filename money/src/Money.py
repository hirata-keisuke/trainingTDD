from abc import abstractmethod, ABCMeta

class Money(metaclass=ABCMeta):

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    @abstractmethod
    def times(amount: int):
        pass

    @classmethod
    def dollar(self, amount: int):
        return Dollar(amount)

    @classmethod
    def franc(self, amount: int):
        return Franc(amount)

class Dollar(Money):

    def __init__(self, amount: int):
        super().__init__(amount)
        
    def times(self, multiplier: int):
        return self.__class__(self._amount * multiplier)
        
class Franc(Money):

    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return self.__class__(self._amount * multiplier)