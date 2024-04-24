# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json

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


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result_task2.json','w',encoding='utf-8') as f:
            json.dump(self._history, f)



    @property
    def history(self):
        return self._history

if __name__ == '__main__':
    a = Factorial(3)

    with a as fact:
        print(fact(3))
        print(fact(4))
        print(fact(5))
        print(fact(6))

