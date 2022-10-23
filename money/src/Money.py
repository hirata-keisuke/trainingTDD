class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.__dict__ == other.__dict__
        return False