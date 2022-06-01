class Item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value  = value
        self.profit = self.value/self.weight

    def __str__(self):
        return f"Item(weight={self.weight},value={self.value})"

    def __repr__(self):
        return self.__str__()