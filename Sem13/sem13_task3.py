# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f'Ошибка приложения! {self.msg}'


class MyValueError(MyAppException):
    def __init__(self, value: int):
        super().__init__(f'Неверное значение: {value}')


class MyLevelError(MyAppException):
    def __init__(self, level: int):
        super().__init__(f'Ошибка доступа: {level}')