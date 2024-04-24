# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging

FORMAT = '{levelname}\n{asctime}\n{name}\n{msg}'
logging.basicConfig(format=FORMAT,
                    style='{',
                    filename='sem15_task3.log',
                    level=logging.INFO,
                    filemode='a+',
                    encoding='utf8')


def logg(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        result = func(*args, **kwargs)
        file_data = f'{result}: {args}, {kwargs}'
        logger.info(file_data)
        return result
    return wrapper


@logg
def tes(a, b):
    return a + b

if __name__ == '__main__':
    print(tes(5, b=4))