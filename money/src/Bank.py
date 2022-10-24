from money.src.Money import Money

class Bank:

    def __init__(self):
        pass

    def reduce(self, source, to: str):
        if isinstance(source, Money):
            return source
        return source.reduce(to)