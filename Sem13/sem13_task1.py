# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def use_input():
    while True:
        try:
            user = float(input('Введите число: '))
            if int(user) == user:
                return int(user)
            return user
        except ValueError:
            print('Введено не число')

if __name__ == '__main__':
    a = use_input()
    print('Вы ввели: ', a)