# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from sem10_task3 import Person

class Employee(Person):

    DIVIDER_FOR_LEVEL_DEFINITION = 7

    def __init__(self, name: str, surname: str, second_name: str, age: int, id: int):
        super().__init__(name, surname, second_name, age)
        self.id = id if len(str(id)) == 6 else 111111
        #self.level = self.count_level()

    @property
    def count_level(self) -> int:
        return sum(map(int,str(self.id))) % Employee.DIVIDER_FOR_LEVEL_DEFINITION


if __name__ == '__main__':
    b = Employee("Босс","Боссов","Боссович",37,123457)
    print(b.get_age())
    print(b.full_name())
    print(b.count_level)
    b.birthday()
    print(b.get_age())
    b.id = 777777
    print(b.count_level)