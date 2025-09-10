class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity} {self.name}(s) purchased!")
        else:
            print("Not enough stock.")