from money.src.Expression import Expression

class Sum(Expression):
    
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):
        from money.src.Money import Money
        amount = self.augend.reduce(bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def plus(self, addend):
        return None