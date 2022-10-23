from abc import abstractmethod, ABCMeta

class Money:

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if other is None or not Money in other.__class__.mro(): return False
        return self.__dict__ == other.__dict__

    def times(self, amount: int):
        return Money(self._amount*amount, self._currency)

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

class Franc(Money):

    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)