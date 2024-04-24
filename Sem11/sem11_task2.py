# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:

    archive = []

    def __new__(cls, *args):
        instance = super().__new__(cls)
        instance.archive = cls.archive.copy()
        cls.archive.append(instance)
        return instance

    def __init__(self,  num: int, text: str):
        self.num = num
        self.text = text


    def __repr__(self):
        return f'{self.num} {self.text}'


if __name__ == '__main__':

    a = Archive(1, 'a')
    b = Archive(2, 'b')
    c = Archive(3, 'c')
    d = Archive(4, 'd')

    print(a.archive)
    print(b.archive)
    print(c.archive)
    print(d.archive)



