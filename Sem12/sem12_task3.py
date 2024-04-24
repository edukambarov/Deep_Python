# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


class Factorial:
    def __init__(self, *args):
        self.start, self.stop, self.step = 1, 1, 1
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args
        elif len(args) == 3:
            self.start, self.stop, self.step = args

        self.factorial_values = []
        self.current_index = self.start

        for i in range(self.start, self.stop + 1, self.step):
            self.factorial_values.append(self.fact(i))

    def fact(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def __iter__(self):
        self.current_index = self.start
        return self

    def __next__(self):
        if self.current_index <= self.stop:
            result = self.fact(self.current_index)
            self.current_index += self.step
            return result
        else:
            raise StopIteration

    def __str__(self):
        return f"Factorials calculated from {self.start} to {self.stop} with step {self.step}"


if __name__ == '__main__':
    a = Factorial(1,10,2)
    for i in a:
        print(i)
