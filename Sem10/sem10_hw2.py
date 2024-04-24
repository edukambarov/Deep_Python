"""
Лотерея Класс

На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists,
который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Пример выходных данных:
Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""

class LotteryGame:
    def __init__(self, ours: list[int], lottery: list[int]):
        self.ours = ours
        self.lottery = lottery

    def compare_lists(self) -> str:
        # res = []
        # for x in self.ours:
        #     if x in self.lottery:
        #         res.append(x)
        res = [x for x in self.ours if x in self.lottery]
        if len(res) == 0:
            print(f'Совпадающих чисел нет.')
        else:
            print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {len(res)}')


if __name__ == '__main__':
    list_a = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list_b = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

    game = LotteryGame(list_a, list_b)
    matching_numbers = game.compare_lists()