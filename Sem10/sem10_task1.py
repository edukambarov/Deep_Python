# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math


class Circle:

    __Pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def length_of_circle(self):
        return 2 * self.radius * Circle.__Pi

    def area_of_circle(self):
        return Circle.__Pi * self.radius**2


circle_1 = Circle(5)
print(circle_1.area_of_circle())
print(circle_1.length_of_circle())

