from money.src.Money import Money

class Bank:

    def __init__(self):
        self.rate = {}

    def reduce(self, source, to: str):
        return source.reduce(self, to)

    def set_rate(self, src: str, dest: str, rate: int):
        if src not in self.rate.keys():
            self.rate[src] = {}
        if dest not in self.rate[src].keys():
            self.rate[src][dest] = rate
    
    def add_rate(self, src: str, dest: str, rate: int):
        self.set_rate(src, dest, rate)
        self.set_rate(dest, src, 1/rate)

    def calc_rate(self, src: str, dest: str):
        if src == dest: return 1
        return self.rate[src][dest]