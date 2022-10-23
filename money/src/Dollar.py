from money.src.Money import Money

class Dollar(Money):

    def __init__(self, amount: int):
        super().__init__(amount)
        
    def times(self, multiplier: int):
        return self.__class__(self._amount * multiplier)