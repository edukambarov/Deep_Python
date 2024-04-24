# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        total_perimeter = self.perimeter() + other.perimeter()
        new_length = total_perimeter / 4
        return Rectangle(new_length, self.width)

    def __sub__(self, other):
        diff_perimeter = abs(self.perimeter() - other.perimeter())
        new_length = diff_perimeter / 2
        return Rectangle(new_length, self.width)

    def __eq__(self, value: object) -> bool:
        return self.length == value.length and self.width == value.width


class TestCheckRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(5, 3)
        self.rect2 = Rectangle(4, 4)
        self.rect3 = Rectangle(4, 2)

    def test_perimeter(self):
        self.assertEqual(self.rect1.perimeter(), self.rect2.perimeter())

    def test_area(self):
        self.assertEqual(self.rect1.area(), 15)
        self.assertEqual(self.rect2.area(), 16)

    def test_add(self):
        a = self.rect1 + self.rect2
        self.assertTrue(a == Rectangle(8, 3))

    def test_sub(self):
        b = self.rect1 - self.rect3
        self.assertTrue(b == Rectangle(2, 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)