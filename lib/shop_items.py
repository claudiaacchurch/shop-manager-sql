class ShopItem:
    def __init__(self, id, name, unit_price, quantity):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
    
    def __eq__(self, other):
        return (self.id == other.id and
                self.name == other.name and
                abs(self.unit_price - other.unit_price) <= 0.05 and
                self.quantity == other.quantity)
    
    def __repr__(self):
        return f"ShopItem({self.id}, {self.name}, {self.unit_price:.2f}, {self.quantity})"