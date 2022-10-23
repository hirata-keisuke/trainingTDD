from abc import abstractmethod, ABCMeta

class Money:

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    @abstractmethod
    def times(self, amount: int):
        pass

    def currency(self) -> str:
        return self._currency

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")

class Dollar(Money):

    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
        
    def times(self, multiplier: int):
        return Money.dollar(self._amount * multiplier)
        
class Franc(Money):

    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int):
        return Money.franc(self._amount * multiplier)