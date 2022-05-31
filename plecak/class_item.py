class Item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value  = value
        self.profit = self.value/self.weight