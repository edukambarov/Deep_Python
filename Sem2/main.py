# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.


# def diff_dimensions(x: int, d: int) -> int:
#     return -1
#
# number: int = int(input ("Введите число: "))
# base = int(input("Введите основание: "))
# num = number
#
# numbers = []
# remained = base
#
# while remained <= num:
#     numbers.append(num % base)
#     num = num // base
# numbers.append(num)
# numbers.reverse()
#
# print(f'число {number} в {base} системе = {numbers}')
#
# print(f"Двоичное число: {bin(number)}")
# print(f"Восьмеричное число: {oct(number)}")

# number = 255
# num = number
#
# base = 16
# numbers = []
# remained = base
#
# while remained <= num:
#     if num % base == 10:
#         numbers.append('A')
#     elif num % base == 11:
#         numbers.append('B')
#     elif num % base == 12:
#         numbers.append('C')
#     elif num % base == 13:
#         numbers.append('D')
#     elif num % base == 14:
#         numbers.append('E')
#     elif num % base == 15:
#         numbers.append('F')
#     else:
#         numbers.append(num % base)
#     num = num // base
# if num == 10:
#     numbers.append('A')
# elif num == 11:
#     numbers.append('B')
# elif num  == 12:
#     numbers.append('C')
# elif num == 13:
#     numbers.append('D')
# elif num == 14:
#     numbers.append('E')
# elif num == 15:
#     numbers.append('F')
# else:
#     numbers.append(num)
# numbers.reverse()
# res = ''
# if number != 0:
#     for el in numbers:
#         res += str(el)
#
#
# print(f'Шестнадцатеричное представление числа: {res}')
# print(f'Проверка результата: {hex(number)}')



# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.

frac1 = "1/2"
frac2 = "1/3"

import fractions

lst1 = [int(x) for x in frac1.split('/')]
lst2 = [int(x) for x in frac2.split('/')]

denominator = lst1[1] * lst2[1]
sum_numerator = lst1[0] * lst2[1] + lst1[1] * lst2[0]
product_numerator = lst1[0] * lst2[0]

sum_frac = str(sum_numerator) + '/' + str(denominator)
product_frac = str(product_numerator) + '/' + str(denominator)
print(f'Сумма дробей: {sum_frac}')
print(f'Произведение дробей: {product_frac}')
print(f'Сумма дробей: {fractions.Fraction(lst1[0], lst1[1]) + fractions.Fraction(lst2[0], lst2[1])}')
print(f'Произведение дробей: {fractions.Fraction(lst1[0], lst1[1]) * fractions.Fraction(lst2[0], lst2[1])}')
