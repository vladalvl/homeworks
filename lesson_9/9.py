class Clothing:
    def __init__(self, type_, color, size, price=None):
        self.type_ = type_
        self.color = color
        self.size = size
        self.price = price

    @staticmethod
    def clothes():
       print("Нет в наличии")

    @classmethod
    def type_of_clothes(cls, type_, color, size, price):
        return cls(type_, color, size, price)


black_dress = Clothing('dress', 'black', 48, 150)
jumpsuits = Clothing('jumpsuits', 'blue', 50)
jeans = Clothing('jeans', 'white', 40, 590)

print(black_dress.size)
print(jumpsuits.color)
print(jeans.type_.title(), jeans.price)
black_dress.clothes()

