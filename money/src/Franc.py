class Franc:

    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Franc(self.__amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Franc):
            return self.__dict__ == other.__dict__
        return False