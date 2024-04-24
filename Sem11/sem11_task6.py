# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# from functools import total_ordering
#
# @total_ordering
class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length


    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.length > other.length and self.width > other.width:
                new_length = self.length - other.length
                new_width = self.width - other.width
                return Rectangle(new_length, new_width)
            raise ValueError('Неправильное соотношение сторон')
        raise TypeError('Передан объект неподходящего класса')

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return Rectangle(self.length * other, self.width * other)


    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.__hash__ == other.__hash__
        raise TypeError('Передан объект неподходящего класса')

    # def __eq__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.area_of_rectangle() == other.area_of_rectangle()
    #     raise TypeError('Передан объект неподходящего класса')


    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area_of_rectangle() > other.area_of_rectangle()
        raise TypeError('Передан объект неподходящего класса')

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area_of_rectangle() >= other.area_of_rectangle()
        raise TypeError('Передан объект неподходящего класса')


    def __hash__(self):
        return hash(self.perimeter_of_rectangle())

    def area_of_rectangle(self):
        return self.length * self.width

    def perimeter_of_rectangle(self):
        return 2 * (self.length + self.width)


    def __str__(self):
        return f' length = {self.length}, width = {self.width}'


if __name__ == '__main__':
    rectangle1 = Rectangle(3,4)
    rectangle2 = Rectangle(2,3)
    rectangle3 = rectangle1.__add__(rectangle2)
    rectangle4 = rectangle1.__sub__(rectangle2)
    rectangle5 = rectangle1.__mul__(2.5)

    print(rectangle3)
    print(rectangle4)
    print(rectangle5)
    print(rectangle1 == rectangle2)
    # print(rectangle1 != rectangle2)
    # print(rectangle1 > rectangle2)
    # print(rectangle1 < rectangle2)
    # print(rectangle1 >= rectangle2)
    # print(rectangle1 <= rectangle2)

