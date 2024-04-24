# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.


import os
import random
from string import ascii_lowercase, digits

# MIN = -1000
# MAX = 1000
#
# def num_random (rows, file_name):
#     with open(file_name, 'a', encoding="utf-8") as f:
#         for _ in range (rows):
#             int_num = random.randint(MIN, MAX)
#             float_num = random.uniform(MIN, MAX)
#             f.write(f'{int_num}|{float_num}\n')
#
#
# num_random(3, 'result_task1.txt')
#
# with open('result_task1.txt', 'r', encoding="utf-8") as f:
#     [print(i) for i in f]



# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


# VOWELS = 'aeuioy'
# CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
# MAX_LEN = 7
# MIN_LEN = 4
#
# def glue_word(file_name = 'result_task2.txt', num = 5):
#     with open(file_name, 'a', encoding="utf-8") as f:
#         for _ in range (num):
#             letters = []
#             x = random.randint(MIN_LEN, MAX_LEN)
#             vowels_quantity = random.randint(1, x)
#             vowels_x = random.choices(VOWELS, k=vowels_quantity)
#             letters.extend(vowels_x)
#             if vowels_quantity < x:
#                 consonants_x = random.choices(CONSONANTS, k= x - vowels_quantity)
#                 letters.extend(consonants_x)
#             random.shuffle(letters)
#             f.write(f'{"".join(letters).title()}\n')
#
# glue_word()


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# def concat_word_and_numbers (file_name1 = "result_task1.txt", file_name2 = "result_task2.txt", target_file = "result_task3.txt"):
#     count = 0
#     with(
#             open(file_name1, 'r', encoding= "utf-8") as f1,
#             open(file_name2, 'r', encoding= "utf-8") as f2,
#             open(target_file, 'w', encoding="utf-8") as output
#     ):
#         lines_num = sum(1 for i in f1)
#         lines_words = sum(1 for i in f2)
#         for line in range(max(lines_words, lines_num)):
#             num1, num2 = process_file(f1).split('|')
#             f1_product = int(num1) * float(num2)
#             word = process_file(f2).strip()
#             if f1_product < 0:
#                 output.write(f'{word.lower()}||{abs(round(f1_product, 0))}\n')
#             else:
#                 output.write(f'{word.upper()}||{round(f1_product, 0)}\n')
#
#
# def process_file(file):
#     text = file.readline()
#     if not text:
#         file.seek(0)
#         text = file.readline()
#     return text.strip()
#
#
# concat_word_and_numbers()


# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


# def genarate_nam_files(ext, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count = 2 ):
#     for _ in range(count):
#         file_nam = "".join(random.choices(ascii_lowercase+digits,k=random.randint(min_len_name, max_len_name)))
#         byte_size = bytes(random.randint(0,255) for i in range(random.randint(min_byte, max_byte)))
#         with open(f"{file_nam}.{ext}", "wb") as file:
#             file.write(byte_size)
#
# genarate_nam_files('txt')


"""
HW1
Функция группового переименования файлов
Напишите функцию группового переименования файлов в папке test_folder 
под названием rename_files.
Она должна:
a. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
Пример использования.
На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
На выходе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
"""
from pathlib import Path

__all__ = ['rename_files']


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):

    work_path = Path.cwd()
    c = 0
    str_0 = str(0) * num_digits
    for p in work_path.iterdir():
        if p.is_file() and str(p.suffix).replace(".","") == source_ext: #str(p)[str(p).index('.') + 1:] == source_ext:#
            c += 1
            file_name = f'{desired_name}' \
                        f'{str(c) if len(str(c)) == num_digits else str_0[:num_digits - len(str(c))] + str(c)}.' \
                        f'{target_ext}'
            p.rename(Path(p.parent, file_name))


import os


def rename_files_2(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
    c = 0
    str_0 = str(0) * num_digits
    for filename in os.listdir("."):
        if filename.endswith(source_ext):
            c += 1
            new_name = f'{desired_name}' \
                        f'{str(c) if len(str(c)) == num_digits else str_0[:num_digits - len(str(c))] + str(c)}.' \
                        f'{target_ext}'
            os.rename(filename, new_name)





if __name__ == '__main__':
    #rename_files("new_file_", 3, "doc", "txt")
    rename_files_2("new_file_", 3, "doc", "txt")

