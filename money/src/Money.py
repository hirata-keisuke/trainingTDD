from money.src.Dollar import Dollar
from money.src.Franc import Franc
from abc import abstractmethod

class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def dollar(amount: int) -> Dollar:
        return Dollar(amount)

    def franc(amount: int) -> Franc:
        return Franc(amount)