# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os
import csv
import pickle

# def create_json(in_file, out_file):
#     with open(in_file, 'r', encoding='UTF-8') as input_file:
#         data = input_file.readlines()
#     data = {row.strip().split('||')[0].capitalize(): float(row.strip().split('||')[1]) for row in data}
#     print(data)
#     with open(out_file, 'w', encoding='UTF-8') as output_file:
#         json.dump(data, output_file, indent=4, ensure_ascii=False)
#
#
# create_json('new_file_005.txt', 'result_task1.json')



# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


# def input_name(msg) -> None:
#     return input(msg)
#
#
# def input_lvl(msg: str, error_message: str, limits=tuple[int]) -> str:
#     while True:
#         level = input(msg)
#         if level.isdigit() and limits[0] <= int(level) <= limits[1]:
#             return level
#         print(error_message)
#
# def input_id(msg: str, error_message: str, id_already_exists: str, id_list = list[str]) -> str:
#     while True:
#         user_id = input(msg)
#         if user_id.isdigit():
#             if user_id not in id_list:
#                 return user_id
#             else:
#                 print(id_already_exists)
#         else:
#             print(error_message)
#
#
# def input_user(file_name: str) -> None:
#     if os.path.exists(file_name):
#         with open(file_name, "r", encoding="utf-8") as f:
#             users_dict = json.load(f)
#     else:
#         users_dict = {}
#     users_id_list = [u_id for users in users_dict.values() for u_id in users]
#     while True:
#         user_name = input_name('Enter the name of user:\n')
#         if not user_name:
#             break
#         user_id = input_id('Enter ID of user:\n',
#                            'ID must consist digits only.',
#                            'User with this ID already exists!',
#                            users_id_list)
#         user_level = input_lvl('Enter access level of user (from 1 to 7):\n',
#                                'Access level must consist digits from 1 to 7 only.',
#                                (1,7))
#         if user_level in users_dict:
#             users_dict[user_level][user_id] = user_name
#         else:
#             users_dict[user_level] = {user_id: user_name}
#         with open(file_name, 'w', encoding='UTF-8') as file:
#             json.dump(users_dict, file, indent=4, ensure_ascii=False, sort_keys=True)
#         users_id_list.append(user_id)
#
#
# input_user('user_list.json')


# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

# def convert_to_csv(json_file, csv_file):
#     with (
#         open(json_file,'r',encoding='utf-8') as users_json,
#         open(csv_file, 'w', encoding='utf-8', newline='') as users_csv,
#     ):
#         data = json.load(users_json)
#         csv_writer = csv.writer(users_csv)
#         csv_writer.writerow(['name','ID','access level'])
#
#         for user_lvl, users in data.items():
#             for user_id, user_name in users.items():
#                 csv_writer.writerow([user_name, user_id, user_lvl])
#
# if __name__ == '__main__':
#     convert_to_csv('user_list.json', 'result_task3.csv')



# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.


# def new_user_json(input_file_name: str, output_file_name: str):
#     with (
#         open(input_file_name,'r', encoding='utf-8') as in_csv_data,
#         open(output_file_name, 'w', encoding='utf-8') as out_json_file
#     ):
#         data = {}
#         csv_reader = csv.reader(in_csv_data)
#         for i, row in enumerate(csv_reader):
#             if i:
#                 user_data = [row[0].lower(), row[1].zfill(10), row[2]]
#                 h = hash(user_data[0] + user_data[1])
#                 data[h] = user_data
#         json.dump(data, out_json_file, indent=4, ensure_ascii=False, sort_keys=True)
#
#
# new_user_json('result_task3.csv','result_task4.json')



# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

# def serialize_json (directory):
#     if not os.path.exists(directory):
#         print(f'Directory "{directory}" was not found.')
#         return
#     files = [file for file in os.listdir(directory) if file.endswith('json')]
#     for file_name in files:
#         json_path = os.path.join(directory, file_name)
#         pickle_path = os.path.join(directory, file_name.split('.')[0] + '.pickle')
#         with (
#             open(json_path, 'r', encoding='utf-8') as json_file,
#             open(pickle_path, 'wb') as pickle_file
#         ):
#             data = json.load(json_file)
#             pickle.dump(data, pickle_file)
#
#
#
# serialize_json('D:\GeekBrains\Погружение в Python\Sem8')


# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.


# def pickle_to_csv(path_pickle: str, headers: list[str]):
#     current_path_pickle = os.path.split(path_pickle)
#     path_csv = os.path.join(current_path_pickle[0], current_path_pickle[-1].split('.')[0] + '.csv')
#     with(
#         open(path_pickle, 'rb') as pickle_file,
#         open(path_csv, 'w', encoding='UTF-8') as csv_file
#     ):
#         data = pickle.load(pickle_file)
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(headers)
#         for user in data.values():
#             csv_writer.writerow(user)
#
#
# pickle_to_csv('result_task4.pickle', ['name','ID','access level'])


# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.


# def print_pickle(path_csv: str):
#     with open(path_csv, 'r', encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         data = [row for row in csv_reader if row]
#         print(pickle.dumps(data))
#
#
# print_pickle('result_task4.csv')



# def get_dir_size(path):
#     size = 0
#     for dirpath, dirnames, filenames in os.walk(path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             size += os.path.getsize(fp)
#     return size
#
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             name = {}
#             name ["Path"] = os.path.join(root, file)
#             name ["Type"] = 'File'
#             name ["Size"] = os.path.getsize(os.path.join(root, file))
#             results.append(name)
#         for dir in dirs:
#             name = {}
#             name["Path"] = os.path.join(root, dir)
#             name["Type"] = 'Directory'
#             name["Size"] = get_dir_size(os.path.join(root, dir))
#             results.append(name)
#     return results
#
#
# def save_results_to_json(results, output_file):
#     with open(output_file, 'w', encoding='utf-8') as res:
#         json.dump(results,res,indent=2,ensure_ascii=False)
#
#
# def save_results_to_csv(results, output_file):
#     keys = results[0].keys()
#     with open(output_file, 'w', newline='', encoding='UTF-8') as output:
#         dict_writer = csv.DictWriter(output, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(results)
#
# def save_results_to_pickle(results, output_file):
#     with open(output_file, 'wb') as pickle_file:
#         pickle.dump(results, pickle_file)
#
#
# directory = 'D:\GeekBrains\Погружение в Python\Sem8'
# results = traverse_directory(directory)
#
# save_results_to_pickle(results, 'results.pkl')
#
# with open('results.pkl', 'rb') as f:
#     data = pickle.load(f)
#     print(data)
#
# save_results_to_csv(results, 'results.csv')
# #
# with open('results.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     data = [row for row in reader]
#
# print(data)

# save_results_to_json(results, 'results.json')
#
# with open('results.json', 'r') as f:
#     data = json.load(f)
#
# print(data)

# code_to_write = '''
# import os
#
# def get_dir_size(path):
#     size = 0
#     for dirpath, dirnames, filenames in os.walk(path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             size += os.path.getsize(fp)
#     return size
#
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             name = {}
#             name ["Path"] = os.path.join(root, file)
#             name ["Type"] = 'File'
#             name ["Size"] = os.path.getsize(os.path.join(root, file))
#             results.append(name)
#         for dir in dirs:
#             name = {}
#             name["Path"] = os.path.join(root, dir)
#             name["Type"] = 'Directory'
#             name["Size"] = get_dir_size(os.path.join(root, dir))
#             results.append(name)
#     return results
#
#
# def save_results_to_json(results, output_file):
#     with open(output_file, 'w', encoding='utf-8') as res:
#         json.dump(results,res,indent=2,ensure_ascii=False)
#
#
# def save_results_to_csv(results, output_file):
#     keys = results[0].keys()
#     with open(output_file, 'w', newline='', encoding='UTF-8') as output:
#         dict_writer = csv.DictWriter(output, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(results)
#
# def save_results_to_pickle(results, output_file):
#     with open(output_file, 'wb') as pickle_file:
#         pickle.dump(results, pickle_file)
# '''
#
# with open("__init__.py", "w") as init_file:
#     init_file.write(code_to_write)