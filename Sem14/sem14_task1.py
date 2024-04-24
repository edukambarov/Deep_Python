# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import re
def del_letter(text: str):
    ascii_letters = re.compile(r'[^a-zA-Z\s]')
    return re.sub(ascii_letters, '',text).lower()

if __name__ == '__main__':
    text = 'hi hiавпор'
    a = del_letter(text)
    print(a)