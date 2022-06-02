# 2.    Создать два класса truck и car, которые являются наследниками класса auto. Класс truck имеет дополнительный
# обязательный атрибут max_load. Переопределнный метод move, перед появлением надписи "move" выводит надпись "attention"
#  А так же дополнительный метод load. При его вызове происходит пауза 1 секунда, затем выдает соообщение
# "load" и снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи "move" должна появиться надпись "max speed is <max_speed>".
# Создать по 2 объекта для каждого из классов truck и car, проверить все методы и атрибуты.
import time


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


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None,  weight=None):
        self.max_load = max_load
        Auto.__init__(self, brand, age, color, mark, weight)

    def move(self):
        print("attention move")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None,  weight=None):
        self.max_speed = max_speed
        Auto.__init__(self, brand, age, mark, color, weight)

    def move(self):
        print("attention move")
        print('max speed is ' + str(self.max_speed))


ford_truck = Truck('Ford', 0, 'Maverick', 2000, 'black')
toyota_truck = Truck('Toyota', 18, 'Tundra', 1575)

bugatti_car = Car('Bugatti', 12, 'Veyron super sport', 434)
ford_car = Car('Ford', 5, 'Mustang', 250)


ford_truck.move()
ford_truck.load()
print(ford_truck.mark)
print(toyota_truck.birthday())
print(toyota_truck.max_load)
toyota_truck.load()

print(bugatti_car.max_speed)
ford_car.move()
bugatti_car.move()




