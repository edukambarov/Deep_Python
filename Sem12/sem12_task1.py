# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


class Factorial:
    def __init__(self, k: int) -> None:
        self.k = k
        self._history = []

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self._history.append((value, result))
        self._history = self._history[-self.k:]
        return result

    @property
    def history(self):
        return self._history

if __name__ == '__main__':
    a = Factorial(3)
    print(a(3))
    print(a(4))
    print(a(5))
    print(a(6))
    print(a.history)