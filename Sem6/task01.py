import random




def _user_input(min_num: int, max_num: int, count: int) -> int:
    while True:
        number = input(f'Введите число от {min_num} до {max_num} (у вас осталось {count} попыток):')
        if number.isdigit() and min_num <= int(number) <= max_num:
            return int(number)
        print(f'Введите число от {min_num} до {max_num}.')


def find_num(min_num: int, max_num: int, count: int):
    random_num = random.randint(min_num, max_num)
    while count:
        user_num = _user_input(min_num, max_num, count)
        if user_num < random_num:
            print('Загаданное число больше!')
        elif user_num > random_num:
            print('Загаданное число меньше!')
        else:
            return True
        count -= 1
    return False

if __name__ == '__main__':
    max_num = 10
    min_num = 1
    count = 3
    find_num(1,10,3)