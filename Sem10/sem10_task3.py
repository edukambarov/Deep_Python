# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:

    def __init__(self, name: str, surname: str, second_name: str, age: int):
        self.name = name
        self.surname = surname
        self.second_name = second_name
        self._age = age

    def full_name(self):
        return f'Ф.И.О.: {self.surname} {self.name} {self.second_name}'

    def birthday(self):
        self._age+=1


    def get_age(self):
        return f'Возраст: {self._age}'

if __name__ == '__main__':
    a = Person("Иван","Иванов","Иванович",39)
    print(a.get_age())
    print(a.full_name())
    a.birthday()
    print(a.get_age())