class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f'Ошибка приложения! {self.msg}'


class MyAccessError(MyAppException):
    def __init__(self, name: str, u_id: str):
        super().__init__(f'Пользователя с таким именем ({name}) и ID({u_id}) не существует!')


class MyLevelError(MyAppException):
    def __init__(self, my_level: int, new_level: int):
        super().__init__(
f'Ошибка доступа! Уровень доступа нового пользователя ({new_level}) меньше вашего уровня ({my_level})')


class MyIDError(MyAppException):
    def __init__(self, u_id: str):
        super().__init__(f'Пользователь с таким ID ({u_id}) уже существует!')


class MyLoginError(MyAppException):
    def __init__(self):
        super().__init__(f'Пользователь не залогирован!')


def is_prime_number(num: int) -> bool:
    '''
    This function return True or False depending on whether the parameter in range is prime number
    '''
    for i in range(2, num):
        if num % i == 0:
            return False
    return True