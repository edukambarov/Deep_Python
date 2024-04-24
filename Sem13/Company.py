# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json

from User import User
from app_exception import *

class Company:
    _company = None
    _file_name = None

    def __new__(cls, name: str = None, db_file: str = 'user_list.json'):
        if cls._company is None:
            cls._company = super().__new__(cls)
            cls._company.name = name
            cls._file_name = db_file
            cls._company._logged_in = None
        return cls._company

    def __init__(self, *args, **kwargs):
        self._logged_in: User | None = None

    @property
    def users_list(self):
        result = set()
        for lvl, user in self._load_json().items():
            for u_id, name in user.items():
                result.add(User(name, u_id, lvl))
        return result

    @classmethod
    def _load_json(cls):
        with open(cls._file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)

    @classmethod
    def _save_json(cls, data: dict):
        with open(cls._file_name, 'w', encoding='UTF-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def _add_new_user(self, new_user: User):
        users_data = self._load_json()
        if str(new_user.lvl) in users_data:
            users_data[str(new_user.lvl)][new_user.id] = new_user.name
        else:
            users_data[str(new_user.lvl)] = {new_user.id: new_user.name}
        self._save_json(users_data)

    def login(self, name: str, u_id: str):
        login_user = User(name, u_id, 0)
        if login_user in self.users_list:
            for user in self.users_list:
                if user == login_user:
                    print(f'Здравствуйте, {user.name}!\nАвторизация прошла успешно! Ваш уровень доступа: {user.lvl}')
                    self._logged_in = user
                    return user.lvl
        raise MyAccessError(name, u_id)

    def logout(self):
        print(f'До свидания, {self._logged_in.name}! До новых встреч!')
        self._logged_in = None

    def new_user(self, user_name: str, u_id: str, new_lvl: int):
        if self._logged_in:
            if new_lvl < int(self._logged_in.lvl):
                raise MyLevelError(self._logged_in.lvl, new_lvl)
            new_user = User(user_name, u_id, new_lvl)
            if new_user in self.users_list:
                raise MyIDError(u_id)
            self._add_new_user(new_user)
        else:
            raise MyLoginError()




if __name__ == '__main__':
    a = Company('GB')
    a.login('Катя', '234')
    a.new_user('Neo', '1', 6)

