# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging


logging.basicConfig(filename='sem15_task2.log',
                    filemode='a+',
    #                 format='{asctime}: {levelname}\n'
    # '{funcName} >> in line {lineno}: {msg}',
                    style='{',
                    level=logging.INFO,
                    encoding='utf-8')

def logg(func):
    def wrapper(*args, **kwargs):
        logging.info(f'{func.__name__} {args} {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__}: {result}')
        return result
    return wrapper

@logg
def find_sum(a,b):
    return a+b


if __name__ == '__main__':
    print(find_sum(5, 4))