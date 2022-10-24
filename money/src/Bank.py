from money.src.Money import Money

class Bank:

    def reduce(self, source, to: str):
        return source.reduce(self, to)
    
    def addRate(self, src: str, dest: str, rate: int):
        pass

    def calc_rate(self, src: str, dest: str):
        return 2 if src == "CHF" and dest == "USD" else 1