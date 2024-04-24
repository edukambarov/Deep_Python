class MyException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class WrongMonth(MyException):
    def __init__(self, month: str):
        super().__init__(f'Месяца {month} не существует!')


class WrongWeekday(MyException):
    def __init__(self, weekday: str):
        super().__init__(f'Дня недели {weekday} не существует!')


class WrongNumber(MyException):
    def __init__(self, month: str, number: int, weekday: str):
        super().__init__(f'В {month} нет {number}-го {weekday}!')