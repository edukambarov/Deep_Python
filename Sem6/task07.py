def _is_leap(current_year: int) -> bool:
    return not current_year % 4 and current_year % 100 or not current_year % 400


def date_validate(user_date: str) -> bool:
    day, month, year = map(int, user_date.split('.'))
    _months = {i: 30 if i in (4, 6, 9, 11) else 31 for i in range(1, 13)}
    _months[2] = 29 if _is_leap(year) else 28
    if 0 < year < 10000 and month in _months and 0 < day <= _months[month]:
        return True
    return False


if __name__ == '__main__':
    print(date_validate('29.02.2024'))
    print(date_validate('29.02.2023'))
    print(date_validate('29.13.2024'))
    print(date_validate('29.02.20245'))



