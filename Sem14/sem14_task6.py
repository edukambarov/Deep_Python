# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.




import pytest

from Sem14.User import User
from Sem14.Company import Company
from Sem13.app_exception import *


@pytest.fixture()
def company():
    return Company('Adidas')


@pytest.fixture()
def user_kate():
    return 'Катя', '234'


@pytest.fixture()
def new_user_17000():
    return 'Василий', '17000', 5


@pytest.fixture()
def new_user_17():
    return 'Василий', '17', 7

@pytest.fixture()
def new_user_1():
    return 'Neo', '1', 7


def test_login_error(company, new_user_17):
    with pytest.raises(MyAccessError):
        company.login(*new_user_17[:2])


def test_new_user_error(company, user_kate, new_user_17000):
    with pytest.raises(MyLevelError):
        company.login(*user_kate)
        company.new_user(*new_user_17000)


def test_id_error(company, user_kate, new_user_1):
    with pytest.raises(MyIDError):
        company.login(*user_kate)
        company.new_user(*new_user_1)


def test_login(company, user_kate):
    assert company.login(*user_kate) == '6'


if __name__ == '__main__':
    pytest.main(['-v'])

