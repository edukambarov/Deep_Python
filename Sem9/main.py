# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
import csv
import random
import json
from typing import Callable
import os
from functools import wraps

# def random_number_game(min_number: int, max_number: int, attempts: int) -> Callable:
#     result_number = random.randint(min_number, max_number)
#     print(f'Guess a number within interval from {min_number} to {max_number}. You have: {attempts} attempts.')
#
#     def check_random():
#         for _ in range(attempts):
#             user_input = int(input(f'Enter your version: '))
#             if user_input == result_number:
#                 print('You did it! Congratulations, number was guessed out!')
#                 return
#             elif user_input < result_number:
#                 print('Guessed number is greater.')
#             else:
#                 print('Guessed number is smaller.')
#         print(f'Unfortunately you have no more attempts. The guessed number was {result_number}.')
#     return check_random
#
# MIN_NUMBER = 1
# MAX_NUMBER = 100
# COUNT = 5
# func = random_number_game(MIN_NUMBER, MAX_NUMBER, COUNT)
# func()


# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

# def validator(func):
#     def wrapper(num: int, attempts: int) -> None:
#         if not 0 < num < 101:
#             num = random.randint(1, 100)
#         if not 0 < attempts < 11:
#             attempts = random.randint(1, 10)
#         return func(num, attempts)
#
#     return wrapper
#
#
# @validator
# def guess_num(num: int, attempts: int) -> None:
#     for attempt in range(attempts):
#         try:
#             guess = int(input(f'Введите целое число от 1 до 100 '
#                                 f'(попытка {attempt + 1} из {attempts}): \n'))
#             if guess == num:
#                 print(f'Вы угадали! Загаданное число - {num}')
#                 break
#             else:
#                 print(f'Вы не угадали!')
#         except ValueError:
#             print('Ошибка ввода, необходимо ввести целое число')
#     else:
#         print(f'Вы проиграли! Загаданное число - {num}')
#
#
# if __name__ == '__main__':
#     guess_num(120, 5)


# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.


# def json_writer(func):
#     def wrapper(*args, **kwargs):
#         file_name = f'{func.__name__}.json'
#         if os.path.exists(file_name):
#             with open(file_name, 'r', encoding='UTF-8') as file:
#                 data_json = json.load(file)
#                 current_id = int(max(data_json)) + 1
#         else:
#             data_json = {}
#             current_id = 1
#             result = func(args, kwargs)
#             data_json[current_id] = {'func_name': func.__name__, 'result': result, 'args': args, 'kwargs': {}}
#             for key, value in kwargs.items():
#                 data_json[current_id]['kwargs'][key] = value
#             with open(file_name, 'w', encoding='UTF-8') as file:
#                 json.dump(data_json, file, indent=4, ensure_ascii=False)
#     return wrapper
#
#
# @json_writer
# def summa_args(*args, **kwargs):
#     return sum(args[0])
#
# summa_args(1,2,3,4, k='6', l='8')
# summa_args(1,3,5,7, m='7', n='9')


# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

# def count(num: int = 1):
#     def deco(func: Callable):
#         def wrapper(*args, **kwargs):
#             counter = []
#             for _ in range(num):
#                 result = func(*args, **kwargs)
#                 counter.append(result)
#             return counter
#         return wrapper
#     return deco
#
# @count(7)
# def rnd(a: int, b: int) -> int:
#     return random.randint(a, b)
#
# print(f'{rnd(1, 10) = }')


# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# Shamil's:
# def save_params(func: Callable):
#
#     def wrapper(*args, **kwargs):
#         params = {
#         "args": args,
#         "kwargs": kwargs
#         }
#         with open("params.json", "w", encoding='utf-8') as file:
#             json.dump(params, file, ensure_ascii=False, indent=4)
#         return func(*args, **kwargs)
#     return wrapper
# def check_range(func: Callable):
#
#     def wrapper(*args, **kwargs):
#         min_number, max_number, count = args
#         if not (1 <= min_number <= 100 and 1 <= max_number <= 100 and 1 <= count <= 10):
#             min_number = random.randint(1, 100)
#             max_number = random.randint(1, 100)
#             count = random.randint(1, 10)
#             print("Числа выходят за пределы диапазона. Используются случайные числа.")
#             print(f"min={min_number}, max={max_number}, count={count}")
#         return func(min_number, max_number, count)
#     return wrapper
# def repeat(times):
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             results = []
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#                 results.append(result)
#             return results
#         return wrapper
#     return decorator
#
# @save_params
# @check_range
# @repeat(2)
# def guess_number_game(min_number: int, max_number: int, count: int) -> int:
#     secret_number = random.randint(min_number, max_number)
#     print(f"Отгадайте число от {min_number} до {max_number}. У вас {count} попыток.")
#     for _ in range(count):
#         guess = int(input("Введите ваше предположение: "))
#         if guess == secret_number:
#             print("Поздравляем! Вы угадали число!")
#             return 1
#         elif guess < secret_number:
#             print("Загаданное число больше.")
#         else:
#             print("Загаданное число меньше.")
#     print(f"К сожалению, вы исчерпали все {count} попыток. Загаданное число было {secret_number}.")
#     return 0
#
# # Пример использования:
# guess_number_game(1, 100, 2)
# guess_number_game(1, 10, 3)


def counter(number):
    def outter(func):
        result = []

        def inner(*args, **kwargs):
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return result

        return inner

    return outter


def json_writer(func):
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data_json = json.load(file)
                current_id = int(max(data_json, key=lambda x: int(x))) + 1
        else:
            data_json = {}
            current_id = 1
        result = func(*args, **kwargs)
        data_json[current_id] = {'func_name': func.__name__, 'result': result, 'args': args, 'kwargs': {}}
        for key, value in kwargs.items():
            data_json[current_id]['kwargs'][key] = value
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    return wrapper


@counter(5)
@json_writer
def summa_args(*args, **kwargs):
    return sum(map(int, args))


summa_args(1, 2, 8, 8, 9, 78, 90, k='6', l='8', h=78)



# HW#1
# Генерация случайных данных и нахождение корней квадратного уравнения
#
# Создайте функцию generate_csv_file(file_name, rows),
# которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c),
# которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots
# в файле results.json будет сохранена информация о параметрах и
# результатах вычислений для каждой строки данных из CSV-файла.
#
# Пример
# На входе:
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==101)
# На выходе:
# True
# True
# Формат JSON файла определён следующим образом:
#
# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
# ]

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
        with open('results.json', 'w') as f:
            json.dump(result_list, f)
    return wrapper

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

generate_csv_file('input_data.csv', 101)
find_roots('input_data.csv')