# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import pytest as pytest


from string import ascii_letters

def not_punctuation(texts):
    return "".join(text for text in texts if text in ascii_letters or text == " ").lower()



def test_no_changes():
    assert 'python python' == not_punctuation('python python')


def test_from_upper_to_lower():
    assert 'python python' == not_punctuation('Python Python')


def test_omit_punctuation():
    assert 'Python, Pyt,hon' != not_punctuation('Python, Pyt,hon')


def test_not_ascii_letters():
    assert 'python ' == not_punctuation('python Пайтон')


def test_all_possible_issues():
    assert 'python ' == not_punctuation('Python, Пайтон/24')


if __name__ == '__main__':
    pytest.main(['-v'])
