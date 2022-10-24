from abc import abstractmethod
from money.src.Expression import Expression
from money.src.Sum import Sum

class Money(Expression):

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if other is None or not Money in other.__class__.mro(): return False
        return self.__dict__ == other.__dict__

    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def times(self, amount: int):
        return Money(self._amount*amount, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend):
        return Sum(self, addend)
    
    def reduce(self, bank, to: str):
        rate = 2 if self._currency == "CHF" and to == "USD" else 1
        return Money(self._amount / rate, to)