# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

# data = "12/234/356/789/99"
# # 1st way
# symbols = [int(x) for x in data.split('/')]
# res = {symbols[1]: symbols[0], symbols[2]: tuple(symbols[3:])}
# print(res)
# # 2nd way
# value1, key1, key2, *value2 = map(int, data.split('/'))
# print(my_dict := {key1: value1, key2: value2})
# =============================================================

# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.
# =============================================================

# data = "От топота копыт пыль по полю летит"
# res = {x: ord(x) for x in list(set(x for x in data.lower().replace(' ', '')))}
# print(res)
# res1 = {x: ord(x) for x in data}
# print(res1)

# =============================================================
# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.
# =============================================================

# print(res1)
# ans = iter(res1.items())
# for _ in range(5):
#     print(next(ans))
#
# print(_ for _ in range(5))

# =============================================================
# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.
# =============================================================

# my_gen = (x for x in range (0, 101, 2) if x // 10 + x % 10 != 8)
# my_gen1 = (x for x in range (0, 101, 2) if sum(map(int, str(x)))!= 8)
# print(*my_gen)
# print(*my_gen1)

# =============================================================
# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.
# =============================================================

# my_gen = ("FizzBuzz" if x % 5 == 0 and x % 3 == 0
#           else "Buzz" if x % 5 == 0
#         else "Fizz" if x % 3 == 0
#           else x for x in range (1,101))
# print(*my_gen, sep='\n')

# =============================================================
# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку
# =============================================================

# print('\n\n'.
#       join(['\n'.
#            join(['\t\t'.
#                 join([f'{x:^3}x{y:^3}= {x*y:^3}'
#                       for x in range(2+k,6+k)])
#                  for y in range(2,11)])
#             for k in (0,4)]))

# =============================================================
# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
# =============================================================

# def prime_numbers_func ():
#     number = 0
#     while True:
#         number += 1
#         if number in [1, 2, 3]:
#             yield number
#             continue
#         if not number % 2:
#             continue
#         for dev in range (3, int(number ** 0.5) + 1, 2):
#             if not number % dev:
#                 break
#         else:
#             yield number
#
#
# gen = prime_numbers_func()
# for _  in range (10):
#     print(next(gen))

# =============================================================
# HW1
# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
# =============================================================

# def get_file_info (file_path):
#     a =max([i for i in range(len(file_path)) if file_path[i] == '/'],default= -1)
#     b = max([j for j in range(len(file_path)) if file_path[j] == '.'], default= -1)
#     if a >= 0:
#         return file_path[:a+1], file_path [a+1:b], file_path[b:]
#     else:
#         return '', file_path [a+1:b], file_path[b:]
#
#
# path = "D:\\GeekBrains\\conflict.bmp"
# print(get_file_info(path))

# =============================================================
# HW2
# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
# =============================================================#

# employees = ['Иван','Сергей','Тамара']
# basic_salary = [30000, 50000, 40000]
# bonus = ['12.5%', '25%', '6.25%']
# res = {k: v for k, v in zip(employees, [x * y for x,y in zip(basic_salary, list(map(lambda b: 0.01 * float(b.replace('%', '')), bonus)))])}
# print(res)

# =============================================================
# HW3
# Создайте
# функцию
# генератор
# чисел
# Фибоначчи(см.Википедию).
# =============================================================

def fib_func():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib_func()
for _ in range(10):
    print(next(gen))




