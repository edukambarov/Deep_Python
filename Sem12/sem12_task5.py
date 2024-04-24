# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    """Класс создает объект - прямоугольники"""

    __slots__ = ['_length','_width']

    def __init__(self, length, width=0) -> None:
        self._length = length
        self._width = width if width else length

    def perimeter(self):
        """Вычисление периметра прямоугольнка"""
        return 2 * (self._width + self._length)

    def area(self):
        """Вычисление площади прямоугольнка"""
        return self._width * self._length

    def __add__(self, other):
        """Сложение сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            new_length = self._length + other._length
            new_width = self._width + other._width
            return Rectangle(new_length, new_width)
        raise ValueError("Ошибка класса")

    def __sub__(self, other):
        """Вычитание сторон двух прямоугольников"""
        if isinstance(other, Rectangle):
            if self._length > other._length and self._width > other._width:
                return Rectangle(self._length - other._length, self._width - other._width)
            raise ValueError("Неверное соотношение сторон")
        raise ValueError("Ошибка класса")

    def __mul__(self, other):
        """Умножение сторон прямоугольнка на число"""
        if isinstance(other, (int, float)):
            return Rectangle(self._length * other, self._width * other)

    def __str__(self) -> str:
        return f"length = {self._length} width = {self._width}"

    def __eq__(self, other):
        """Сравнение площадей двух прямоугольников на равенство"""
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise ValueError("Ошибка класса")

    def __gt__(self, other):
        """Сравнение площадей двух прямоугольников (первый больше второго)"""
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        raise ValueError("Ошибка класса")

    def __ge__(self, other):
        """Сравнение площадей двух прямоугольников (первый не больше второго)"""
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        raise ValueError("Ошибка класса")

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Длина должна быть положительной.')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Ширина должна быть положительной.')


if __name__ == '__main__':
    rectangle1 = Rectangle(3, 4)
    rectangle1.color = 'red'