from abc import abstractmethod, ABCMeta

class Money:

    def __init__(self, _amount: int, _currency: str):
        self._amount = _amount
        self._currency = _currency

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    @abstractmethod
    def times(self, amount: int):
        pass

    def currency(self) -> str:
        return self._currency

    @classmethod
    def dollar(self, amount: int):
        return Dollar(amount)
    @classmethod
    def franc(self, amount: int):
        return Franc(amount)

class Dollar(Money):

    def __init__(self, amount: int):
        super().__init__(amount, "USD")
        
    def times(self, multiplier: int):
        return self.__class__(self._amount * multiplier)
        
class Franc(Money):

    def __init__(self, amount: int):
        super().__init__(amount, "CHF")

    def times(self, multiplier: int):
        return self.__class__(self._amount * multiplier)