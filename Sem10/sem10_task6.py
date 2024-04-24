# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.
from typing import Any


class Animal:

    def __init__(self, name: str, age: int, spec: Any):
        self.name = name
        self.age = age
        self.spec = spec

    def __str__(self):
        return f'Name:{self.name}, age:{self.age}'


    def specific_property(self):
        return self.spec


class Dog(Animal):

    def __init__(self, name: str, age: int, voice: str):
        super().__init__(name, age, voice)
        self.voice = voice


class Salmon(Animal):

    def __init__(self, name: str, age: int, dive_depth: int):
        super().__init__(name, age, dive_depth)
        self.dive_depth = dive_depth


class Eagle(Animal):

    def __init__(self, name: str, age: int, wingspan: int):
        super().__init__(name, age, wingspan)
        self.wingspan = wingspan


if __name__ == '__main__':
    dog1 = Dog("Tuzik", 3, "bark")
    eagle1 = Eagle("Orlik", 4, 100)
    salmon1 = Salmon("Filadelfia", 2, 50)
    print(dog1.spec)
    print(dog1.voice)
    print(dog1.specific_property())