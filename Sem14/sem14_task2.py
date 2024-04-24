# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters

def not_punctuation(texts):
    """
    >>> not_punctuation("python python")
    'python python'
    >>> not_punctuation("Python Python")
    'python python'
    >>> not_punctuation("Python, Pyt,hon")
    'python python'
    >>> not_punctuation("python Пайтон")
    'python '
    >>> not_punctuation("Python, Пайтон/24")
    'python '
    """
    return "".join(text for text in texts if text in ascii_letters or text == " ").lower()



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)