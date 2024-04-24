# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


from collections import namedtuple
import os
import logging
import argparse

logging.basicConfig(filename='D:\\GeekBrains\\Deep Python\\Sem15_homework\\task_log.log',
                    filemode='a+',
                    level=logging.NOTSET,
                    encoding='utf-8')


def log_deco(func):
    def wrapper(*args):
        logger = logging.getLogger(func.__name__)
        result = func(*args)
        result_formatted = '\n'.join((str(x).replace('Content', '') for x in result))
        file_data = f'{args}:\n{result_formatted}'
        logger.info(file_data)
        return result
    return wrapper


@log_deco
def traverse_directory(path: str) -> list:
    Content = namedtuple('Content', ['name', 'extension', 'dir_flag', 'parent_dir'])
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            parent_dir = os.path.join(root)
            dir_flag = os.path.isdir(file)
            name_full = os.path.basename(file)
            name, file_extension = os.path.splitext(name_full)
            c = Content(name, file_extension, dir_flag, parent_dir)
            result.append(c)
        for dir in dirs:
            parent_dir = os.path.join(root)
            dir_flag = os.path.isdir(os.path.join(root, dir))
            name = os.path.basename(dir)
            file_extension = 'dir'
            c = Content(name, file_extension, dir_flag, parent_dir)
            result.append(c)
    return result


parser = argparse.ArgumentParser(description="информация о содержимом папки")
parser.add_argument('directory', help="Введите абсолютный путь к папке", type=str)
parser.add_argument('--function', default=traverse_directory)
args = parser.parse_args()
args.function(args.directory)


# if __name__ == '__main__':
#     directory = 'D:\\GeekBrains\\Deep Python\\Sem15'
#     traverse_directory(directory)
