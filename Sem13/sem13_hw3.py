# Управление информацией о сотрудниках и их возраст
#
#
# В организации есть два типа людей:
# сотрудники и
# обычные люди.
#
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая)
# Имя (строка, не пустая)
# Отчество (строка, не пустая)
# Возраст (целое положительное число)
#
# Сотрудники имеют также
# уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person,
# который будет иметь атрибуты
# и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
#
# Класс должен проверять валидность входных данных
# и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.



# Создать класс Employee,
# который будет наследовать класс Person и
# добавлять уникальный идентификационный номер (ID).

# Класс Employee также должен проверять валидность ID и
# генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person,
# который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee,
# который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.

#from numpy.core.defchararray import zfill
class InvalidNameError(Exception):
    def __init__(self, text: str):
        self.text = text
    def __str__(self):
        return f'Invalid name: {self.text}. Name should be a non-empty string.'


class InvalidAgeError(Exception):
    def __init__(self, num: int):
        self.num = num
    def __str__(self):
        return f'Invalid age: {self.num}. Age should be a positive integer.'


class InvalidIdError(Exception):

    def __init__(self, id: int):
        self.id = id
    def __str__(self):
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, last_name: str, first_name: str, patronic_name: str, age: int):
        if not isinstance(last_name, str) or len(last_name) == 0:
            raise InvalidNameError(last_name)
        self.last_name = last_name
        if not isinstance(first_name, str) or len(first_name) == 0:
            raise InvalidNameError(first_name)
        self.first_name = first_name
        if not isinstance(patronic_name, str) or len(patronic_name) == 0:
            raise InvalidNameError(patronic_name)
        self.patronic_name = patronic_name
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Employee(Person):

    DIVIDER_FOR_LEVEL_DEFINITION = 7

    def __init__(self, last_name: str, first_name: str, patronic_name: str, age: int, id: int):
        super().__init__(last_name, first_name, patronic_name, age)
        if not isinstance(id, int) or len(str(id)) != 6:
            raise InvalidIdError(id)
        self.id = id

    @property
    def get_level(self) -> int:
        return sum(map(int, str(self.id))) % Employee.DIVIDER_FOR_LEVEL_DEFINITION


if __name__ == '__main__':
    b = Employee("Босс", "Боссов", "Боссович", 37, 123456)
    print(b.id)
    print(b.get_level)
