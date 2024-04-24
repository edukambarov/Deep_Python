# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Dog:

    def __init__(self, name: str, age: int, voice: str):
        self.name = name
        self.age = age
        self.voice = voice

    def specific_property(self):
        return self.voice

    def __str__(self):
        return f'Name:{self.name}, age:{self.age}'

class Salmon:

    def __init__(self, name: str, age: int, dive_depth: int):
        self.name = name
        self.age = age
        self.dive_depth = dive_depth

    def specific_property(self):
        return self.dive_depth

    def __str__(self):
        return f'Name:{self.name}, age:{self.age}'


class Eagle:

    def __init__(self, name: str, age: int, wingspan: int):
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def specific_property(self):
        return self.wingspan

    def __str__(self):
        return f'Name:{self.name}, age:{self.age}'



if __name__ == '__main__':
    all_the_staff = []
    dog1 = Dog("Tuzik", 3, "bark")
    all_the_staff.append(dog1)
    eagle1 = Eagle("Orlik", 4, 100)
    all_the_staff.append(eagle1)
    salmon1 = Salmon("Filadelfia", 2, 50)
    all_the_staff.append(salmon1)
    for x in all_the_staff:
        print(x)
        print(x.specific_property())





