from money.src.Money import Money

class Bank:

    def __init__(self):
        pass

    def reduce(self, source, to):
        amount = source.augend._amount + source.addend._amount
        return Money(amount, to)