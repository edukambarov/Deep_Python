import time
import datetime


# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

class MyString(str):
    def __new__(cls, string,author=None):
        data = super().__new__(cls,string)
        data.author = author
        # data.time = time.time()
        data.time_new = datetime.datetime.now()
        return data

if __name__ == '__main__':

    my_string = MyString('Рок н ролл',author='Stoun')

    print(my_string)
    print(my_string.author)
    # print(my_string.time)
    print(my_string.time_new)