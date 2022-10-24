from money.src.Money import Money

class Bank:

    def reduce(self, source, to: str):
        return source.reduce(to)
    
    def addRate(self, src: str, dest: str, rate: int):
        pass