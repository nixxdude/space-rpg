class Ore:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.sell_price = round(rarity * 5)
