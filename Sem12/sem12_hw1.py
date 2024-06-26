# Работа с данными студентов

# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию, выведите:
#
#
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Если такого предмета нет, выведите: #
# Предмет {Название предмета} не найден

# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# В противном случае выведите:#
# Оценка должна быть целым числом от 2 до 5#
# Результат теста должен быть целым числом от 0 до 100

# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
# по оценкам всех предметов вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы.
# Сейчас в файл записана следующая информация.#
# Математика,Физика,История,Литература

# Создайте класс Student,
# который будет представлять студента и его успехи по предметам.
# Класс должен иметь следующие методы:
# Атрибуты класса:
#
# name (str): ФИО студента.
# subjects (dict): Словарь, который хранит предметы в качестве ключей
# и информацию об оценках и результатах тестов для каждого предмета в виде словаря.
#
# Магические методы (Dunder-методы):#
# __init__(self, name, subjects_file): Конструктор класса.
# Принимает имя студента и файл с предметами и их результатами.
# Инициализирует атрибуты name и subjects и
# вызывает метод load_subjects для загрузки предметов из файла.
#
# __setattr__(self, name, value):
# Дескриптор, который проверяет установку атрибута name.
# Убеждается, что name начинается с заглавной буквы и состоит только из букв.
#
# __getattr__(self, name):
# Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
#
# __str__(self):
# Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
#
# Методы класса:#
# load_subjects(self, subjects_file):
# Загружает предметы из файла CSV.
# Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
#
# add_grade(self, subject, grade):
# Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.
#
# add_test_score(self, subject, test_score):
# Добавляет результат теста по заданному предмету.
# Убеждается, что результат теста является целым числом от 0 до 100.
#
# get_average_test_score(self, subject):
# Возвращает средний балл по тестам для заданного предмета.
#
# get_average_grade(self):
# Возвращает средний балл по всем предметам.
#
# Пример#
# На входе:#
# student = Student("Иван Иванов", "subjects.csv")#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)#
# student.add_grade("История", 5)
# student.add_test_score("История", 92)#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")#
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")#
# print(student)

# На выходе:#
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История

import csv

class Student:

    # __slots__ = ['_name','subjects']
    def __init__(self, name: str, subjects_file: str):
        self._name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file: str):
        with open(subjects_file, 'r', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for ele in row:
                    self.subjects[ele] = {}

    def __setattr__(self, name: str, value):
        if name == "_name":
            if all(char.isalpha() for char in [char for char in value.replace(' ', '')]) \
                    and all([x.istitle() for x in value.split()]):
                return super().__setattr__(name, value)
            else:
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            return super().__setattr__(name, value)

    def __getattr__(self, name):
        return self.subjects[name]

    def __str__(self):
        mentioned_subjects = ", ".join([x for x in self.subjects.keys() if self.subjects[x] != {}])
        return f'Студент: {self._name}\nПредметы: {mentioned_subjects}'

    def add_test_score(self, subject: str, test_score: int):
        if isinstance(test_score, int):
            if 0 <= test_score <= 100:
                if 'test_scores' not in getattr(self, subject).keys():
                    getattr(self, subject)['test_scores'] = []
                getattr(self, subject)['test_scores'].append(test_score)
            else:
                raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        if subject not in self.subjects.keys():
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject) -> float:
        if subject not in self.subjects.keys():
            raise ValueError(f'Предмет {subject} не найден')
        else:
            return round(sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores']), 1)

    def add_grade(self, subject: str, grade: int):
        if isinstance(grade, int):
            if 2 <= grade <= 5:
                if 'grades' not in getattr(self, subject).keys():
                    getattr(self, subject)['grades'] = []
                getattr(self, subject)['grades'].append(grade)
            else:
                raise ValueError(
                    'Оценка должна быть целым числом от 2 до 5')
        if subject not in self.subjects.keys():
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self) -> float:
        marks = []
        for x in self.subjects.values():
            if x != {}:
                marks.extend(x['grades'])
        return round(sum(marks) / len(marks), 1)

# Решение GB:
#     def __init__(self, name, subjects_file):
#         self.name = name
#         self.subjects = {}
#         self.load_subjects(subjects_file)
#
#
#     def __setattr__(self, name, value):
#         if name == 'name':
#             if not value.replace(' ', '').isalpha() or not value.istitle():
#                 raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
#         super().__setattr__(name, value)
#
#
#     def __getattr__(self, name):
#         if name in self.subjects:
#             return self.subjects[name]
#         else:
#             raise AttributeError(f"Предмет {name} не найден")
#
#
#     def __str__(self):
#         return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"
#
#
#     def load_subjects(self, subjects_file):
#         with open(subjects_file, 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 subject = row[0]
#                 if subject not in self.subjects:
#                     self.subjects[subject] = {'grades': [], 'test_scores': []}
#
#
#     def add_grade(self, subject, grade):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(grade, int) or grade < 2 or grade > 5:
#             raise ValueError("Оценка должна быть целым числом от 2 до 5")
#         self.subjects[subject]['grades'].append(grade)
#
#
#     def add_test_score(self, subject, test_score):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
#             raise ValueError("Результат теста должен быть целым числом от 0 до 100")
#         self.subjects[subject]['test_scores'].append(test_score)
#
#
#     def get_average_test_score(self, subject):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден")
#         test_scores = self.subjects[subject]['test_scores']
#         if len(test_scores) == 0:
#             return 0
#         return sum(test_scores) / len(test_scores)
#
#
#     def get_average_grade(self):
#         total_grades = []
#         for subject in self.subjects:
#             grades = self.subjects[subject]['grades']
#             if len(grades) > 0:
#                 total_grades.extend(grades)
#         if len(total_grades) == 0:
#             return 0
#         return sum(total_grades) / len(total_grades)


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    student.add_grade("История", 3)
    student.add_test_score("История", 64)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("История")
    print(f"Средний результат по тестам по математике: {average_test_score}")


