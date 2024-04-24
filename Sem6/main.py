# Задание №1
# � Вспомните какие модули вы уже проходили на курсе.
# � Создайте файл, в котором вы импортируете встроенные в
# модуль функции под псевдонимами. (3-7 строк импорта).
import random

import math as ma

from cffi.backend_ctypes import xrange
from pandas import pivot as pvt, plotting as plt
from sys import base_exec_prefix as bep
#from itertools import *
from Sem6 import find_num
from Sem6 import date_validate

# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь




# Задание №3
# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.



# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.



# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.



# Задание №6
# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение


# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию



# Задание №8
# � Создайте пакет с всеми модулями, которые вы создали за
# время занятия.
# � Добавьте в __init__ пакета имена модулей внутри дандер
# __all__.
# � В модулях создайте дандер __all__ и укажите только те
# функции, которые могут верно работать за пределами
# модуля

# # HW №1
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2),
# проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.
# Не забудьте напечатать результат.


# def is_attacking_my (q1, q2) -> bool:
#     if abs(q1[0] - q2[0]) > 0 and abs(q1[1] - q2[1]) > 0 and abs(q1[0] - q2[0])!=abs(q1[1] - q2[1]):
#         return True
#     return False
#
#
# def check_queens_my (queens) -> bool:
#     for w in range(len(queens)-1):
#         for b in range(len(queens[w+1:])):
#             if not is_attacking(queens[w],queens[b]):
#                 return False
#                 break
#     return True


from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# queens2 = [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]
# print(check_queens(queens))
# print(check_queens(queens2))

# # HW №2
# Расстановка ферзей
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается
# такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
#
# Пример использования
# На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

# board_list = []
# answer = [(tuple(random.randint(1,8) for _ in range(2))) for _ in range(8)]
# print(answer)
# print(check_queens(answer))
# print(check_queens([(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]))

# board_list = []
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# all_positions = list(combinations(x,2))
# while True:
#     unavailable_positions = []
#     result = []
#     q1 = random.choice(all_positions)
#     unavailable_positions.append(q1)
#     result.append(q1)
#     for x in all_positions:
#         if is_attacking(q1, x):
#             unavailable_positions.append(x)
#     available_positions = [x for x in all_positions if x not in unavailable_positions]
#     for _ in range (7):
#         if available_positions:
#             q = random.choice(available_positions)
#             unavailable_positions.append(q)
#             result.append(q)
#             for x in available_positions:
#                 if is_attacking(q, x):
#                     unavailable_positions.append(x)
#             available_positions = [x for x in all_positions if x not in unavailable_positions]
#     if len(result) == 8:
#         board_list.append(result)
#     if len(board_list) == 4:
#         break
# print(board_list)

def generate_board():
    # Генерируем случайную доску
    board = []
    for i in range(1, 9):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list


print(generate_boards())


# import itertools
#
# def queens():
#     for p in itertools.permutations(range(1,9)):
#         yield [x for x in enumerate(p)]

# def generate_boards_2():
#     board_list = []
#     for q in queens():
#         err = False
#         for a, b in ((a, b) for a in q for b in q if a[0] < b[0]):
#             if abs(a[0] - b[0]) == abs(a[1] - b[1]):
#                 err = True
#                 break
#         if not err: board_list.append(q)
#     return board_list[:4]
#
#
# print(len(generate_boards_2()))




# HW №3
# Проверка корректности даты
# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна) или
# "False" (дата некорректна) в зависимости от результата проверки.
#
# Пример использования
# На входе:
# date_to_prove = 15.4.2023
# На выходе:
# True
# На входе:
# date_to_prove = 31.6.2022
# На выходе:
# False


# def _is_leap(current_year: int) -> bool:
#     return not current_year % 4 and current_year % 100 or not current_year % 400
#
#
# def date_validate(user_date: str) -> bool:
#     day, month, year = map(int, user_date.split('.'))
#     _months = {i: 30 if i in (4, 6, 9, 11) else 31 for i in range(1, 13)}
#     _months[2] = 29 if _is_leap(year) else 28
#     if 0 < year < 10000 and month in _months and 0 < day <= _months[month]:
#         return True
#     return False
#
#
# date_to_prove = 15.4.2023
# print(date_validate(date_to_prove))