# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def area_of_rectangle(self):
        return self.length * self.width

    def perimeter_of_rectangle(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    rectangle1 = Rectangle(3,4)
    square1 = Rectangle(4)
    print(rectangle1.area_of_rectangle())
    print(square1.perimeter_of_rectangle())

