# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки

# =============================================================

# def split_and_print(words: str):
#     words_ = words.lower().split()
#     max_len = len(max(words_,key = len))
#     for num, word in enumerate(words_,1):
#         print(f'{num:>{1+len(words_)//10}} {word:>{max_len}}')
#
#
# sentence = "I prefer to have a workout at home rather than go to gym"
# split_and_print(sentence)

# =============================================================

# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# =============================================================

# def get_unicode(words: str) -> list:
#     words_ = [symbol for symbol in words.lower() if symbol != ' ']
#     lst = sorted([ord(x) for x in list(set(words_))], reverse=True)
#     return lst
#
#
# sentence = "I prefer to have a workout at home rather than go to gym"
# print(get_unicode(sentence))
#
# =============================================================
#
# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
#
# =============================================================

# def get_dict_from_unicode(text: str) -> dict:
#     numbers = sorted([int(x) for x in text.split() if x.isdigit()])
#     res = {chr(x): x for x in range(numbers[0],numbers[-1]+1)}
#     return res
#
# example = '10 15'
# print(get_dict_from_unicode(example))

# =============================================================
# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
# =============================================================
# def merge_sort(nums: list) -> list:
#     if len(nums) > 1:
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k] = right[j]
#             j+=1
#             k+=1
#     return nums
#
#
# lst = [5, 2, 7, 4, 8, 1, 6, 3]
# print(merge_sort(lst))
# =============================================================
#
# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
# =============================================================

# def get_bonus_payment(names: list, salary_rate: list, bonus: list) -> dict:
#     bonus_coef = list(map(lambda b: 0.01 * float(b.replace('%', '')), bonus))
#     res = {k: v for k, v in zip(names, [x * y for x,y in zip(salary_rate, bonus_coef)])}
#     return res
#
#
# employees = ['Иван','Сергей','Тамара']
# basic_salary = [30000, 50000, 40000]
# bonus = ['12.5%', '25%', '6.25%']
# print(get_bonus_payment(employees, basic_salary, bonus))
# =============================================================
#
# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
#  =============================================================

# def find_sum_bw_two_indeces (lst: list, start: int, finish: int) -> int:
#     if finish > len(lst):
#         res = sum(lst[start+1:])
#     if start < 0:
#         res = sum(lst[:finish])
#     res = sum(lst[start+1: finish])
#     return res
#
#
# numbers = [1,2,3,4,5,6]
# print(find_sum_bw_two_indeces(numbers, -1, 14))
#  =============================================================
#
# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
#  =============================================================

# def check_profitability (items: dict) -> bool:
#     for k,v in items.items():
#         if sum(v) < 0:
#             return False
#     return True
#
#
# companies = {'A':[1000,-100,-200,-300],
#              'B':[1100,-200,-300,-400],
#              'B':[1300,-300,-400,-700]}
#
# print(check_profitability(companies))

#  =============================================================
#
# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
#  ===========================================================

# numbers = '123'
# names = 'James'
#
#
# def find_and_change_symbol ():
#     temp = {}
#     for key, value in globals().items():
#         if key.endswith('s') and len(value) > 1:
#             temp[key[:-1]] = value
#             temp[key] = None
#     #return [x[:-1] + x[-1].replace('s','None') if x.endswith('s') and len(x) > 1 else x for x in lst]
#     globals().update(temp)
#
# find_and_change_symbol()
#
# print(name)
# print(names)
# print(number)
# print(numbers)

#  ===========================================================
#
# ДЗ 1
# Транспонирование матрицы
#
# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
#
# Пример использования На входе:
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
#
# На выходе:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#  ===========================================================

# def transpose(matrix: list) -> list:
#     res = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             res[j][i] = matrix[i][j]
#     return res
#
#
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# print(transposed_matrix)


#  ===========================================================
#
# ДЗ 2
# Преобразование ключей и значений словаря
# Напишите функцию key_params,
# принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
#  ===========================================================

# def key_params (**kwargs) -> dict:
#     new_dict = {}
#     for k, v in kwargs.items():
#         if v.__hash__:
#             new_dict[v] = k
#         else:
#             new_dict[str(v)] = k
#     return new_dict
#
# print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))
#  ===========================================================
#
# ДЗ 3
# Преобразование ключей и значений словаря
#
# Задача о банкомате
#
# У вас есть банковская карта с начальным балансом равным 0 у.е.
# Вы хотите управлять этой картой, выполняя следующие операции,
# для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY.
# При снятии средств начисляется комиссия в процентах от снимаемой суммы,
# которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом.
# Перед завершением, если на счету больше RICHNESS_SUM,
# начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет,
# кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом,
# используя библиотеку decimal для точных вычислений.
#
# Пример
# На входе:
# deposit(10000)
# withdraw(4000)
# exit()
# print(operations)
# На выходе:
#  ['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']
# На входе:
# deposit(1000)
# withdraw(200)
# exit()
# print(operations)
# На выходе:
#  ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Возьмите карту на которой 770 у.е.']
# На входе:
# deposit(1000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
# print(operations)
# На выходе:
# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.', 'Пополнение карты на 500 у.е. Итого 940 у.е.', 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.', 'Возьмите карту на которой 940 у.е.']
# На входе:
# deposit(173)
# withdraw(21)
# exit()
# print(operations)
# На выходе:
# Сумма должна быть кратной 50 у.е.
# Сумма должна быть кратной 50 у.е.
# ['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']
# На входе:
# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
# print(operations)
# На выходе:
# ['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.', 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.', 'Снятие с карты 3000 у.е. Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.', 'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.', 'Возьмите карту на которой 899999999997205.5000 у.е.']

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def check_multiplicity(amount: int) -> bool:
    if amount % MULTIPLICITY == 0:
        return True
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False


def deposit(amount: int) -> None:
    global bank_account
    global count
    if check_multiplicity(amount):
        bank_account += amount
        count+=1
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    accrue_dep_interest()

def accrue_dep_interest() -> None:
    global bank_account
    global count
    if count % COUNTER4PERCENTAGES == 0:
        dep_interest = bank_account * PERCENT_DEPOSIT
        bank_account += dep_interest
        operations.append(f'Начислен процент на остаток {dep_interest} у.е. Итого {bank_account} у.е.')


def withdraw_incorrect(amount: int) -> None:
    global bank_account
    check_multiplicity(amount)
    withdrawal_fee = min(max(MIN_REMOVAL, PERCENT_REMOVAL * amount),MAX_REMOVAL)
    if bank_account >= amount + withdrawal_fee:
        bank_account -= (amount+ withdrawal_fee)
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {round(withdrawal_fee,0)} у.е.. Итого {round(bank_account,0)} у.е.')
    else:
        operations.append(f'Недостаточно средств. Сумма с комиссией {round(amount + withdrawal_fee,0)} у.е. На карте {bank_account} у.е.')


def withdraw(amount: int) -> None:
    global bank_account
    global count
    if check_multiplicity(amount):
        withdrawal_fee = min(max(MIN_REMOVAL, PERCENT_REMOVAL * amount),MAX_REMOVAL)
        if bank_account >= amount + withdrawal_fee:
            bank_account -= (amount+ withdrawal_fee)
            count += 1
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {round(withdrawal_fee,0)} у.е.. Итого {round(bank_account,0)} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {round(amount + withdrawal_fee,0)} у.е. На карте {bank_account} у.е.')
    accrue_dep_interest()


def exit() -> None:
    global bank_account
    if bank_account >= RICHNESS_SUM:
        richness_tax = bank_account * RICHNESS_PERCENT
        bank_account -= richness_tax
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {richness_tax} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(150600)
withdraw(150000)
deposit(60600)
withdraw(50000)
exit()
print(operations)
