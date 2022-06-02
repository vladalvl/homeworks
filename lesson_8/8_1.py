# 1.    Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
# А так же методы move, birthday и stop. Методы move и stop выводят сообщение на экран "move" и "stop",
# а birthday увеличивает атрибут age на 1. Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    def __init__(self, brand, age, mark, color=None,  weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("Move")

    def birthday(self):
        self.age += 1
        return self.age

    def stop(self):
        print("Stop")


tesla_auto = Auto('Tesla', 0, 'model 3', 'grey', 1700)
bmw_auto = Auto('BMW', 9, '5 series gt')

print(tesla_auto.weight)
print(bmw_auto.mark)

tesla_auto.move()

print(tesla_auto.age)
print(tesla_auto.birthday())

bmw_auto.stop()
