Class Product:
    Def __init__(self, name, price, stock):
        Self.name = name
        Self.price = price
        Self.stock = stock

    Def purchase(self, quantity):
        If quantity <= self.stock:
            Self.stock -= quantity
            Print(f”{quantity} {self.name}(s) purchased!”)
        Else:
            Print(“Not enough stock.”)
