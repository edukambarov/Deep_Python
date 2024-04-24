# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from sem14_task2 import not_punctuation

class TestNameCase(unittest.TestCase):

    def test_no_changes(self):
        self.assertEqual('python python', not_punctuation('python python'))

    def test_from_upper_to_lower(self):
        self.assertEqual('python python', not_punctuation('Python Python'))

    def test_omit_punctuation(self):
        self.assertNotEqual('Python, Pyt,hon', not_punctuation('Python, Pyt,hon'))

    def test_not_ascii_letters(self):
        self.assertEqual('python ', not_punctuation('python Пайтон'))

    def test_all_possible_issues(self):
        self.assertEqual('python ', not_punctuation('Python, Пайтон/24'))


if __name__ == '__main__':
    unittest.main(verbosity=2)

