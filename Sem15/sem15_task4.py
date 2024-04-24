# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import date, datetime, timedelta
import logging
from exceptions import *


def extract_date_from_text(msg: str):

    data = msg.split(' ')
    preres = []
    if len(data) == 3:
        preres.append(int(data[0][:data[0].index('-')]))
        day_of_week = month = -1
        days_acc = 0
        match data[1]:
            case 'понедельник': day_of_week = 0
            case 'вторник': day_of_week = 1
            case 'среда': day_of_week = 2
            case 'четверг': day_of_week = 3
            case 'пятница': day_of_week = 4
            case 'суббота': day_of_week = 5
            case 'суббота': day_of_week = 6
            case _: pass
        preres.append(day_of_week)
        match data[2][:-1]:
            case 'январ':
                month = 1
            case 'феврал':
                month  = 2
                days_acc = 31
            case 'март':
                month = 3
                days_acc = 60
            case 'апрел':
                month = 4
                days_acc = 91
            case 'ма':
                month = 5
                days_acc = 121
            case 'июн':
                month = 6
                days_acc = 152
            case 'июл':
                month = 7
                days_acc = 182
            case 'август':
                month = 8
                days_acc = 213
            case 'сентябр':
                month = 9
                days_acc = 244
            case 'октябр':
                month = 10
                days_acc = 274
            case 'ноябр':
                month = 11
                days_acc = 305
            case 'декабр':
                month = 12
                days_acc = 335
            case _:
                month = 0
        preres.append(month)
        preres.append(days_acc)
    year_start = date(date.today().year,1,1)
    cur_date_days = preres[3] - year_start.weekday() + preres[1] + (preres[0] - 1) * 7
    start_dt = datetime.combine(year_start, datetime.min.time())
    end_dt = start_dt + timedelta(days = cur_date_days)
    return f'Вы ввели дату: {end_dt.date()}'





def check_date(date_str: str):
    year = datetime.today().year

    def _is_leap(cur_year: int) -> bool:
        return bool(not cur_year % 4 and cur_year % 100 or not cur_year % 400)

    weekdays = [
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье'
    ]
    months = {
    'янв': (31, 1),
    'фев': (29 if _is_leap(year) else 28, 2),
    'мар': (31, 3),
    'апр': (30, 4),
    'мая': (31, 5),
    'май': (31, 5),
    'июн': (30, 6),
    'июл': (31, 7),
    'авг': (31, 8),
    'сен': (30, 9),
    'окт': (31, 10),
    'ноя': (30, 11),
    'дек': (31, 12)

    }
    day, weekday, cur_month = date_str.split()
    day = ''.join([i for i in day if i.isdigit()])
    if cur_month[:3] not in months:
        raise WrongMonth(cur_month)
    month = months[cur_month[:3]]
    if weekday not in weekdays:
        raise WrongWeekday(weekday)
    if day and 0 < int(day) <= 5:
        cur_day, day = int(day), int(day)
    else:
        raise WrongNumber(cur_month, day, weekday)
    cur_weekday, weekday = weekday, weekdays.index(weekday)
    first_day = datetime.strptime(f'01-{str(month[1]).zfill(2)}-{year}', '%d-%m-%Y').weekday()
    for i in range(month[0]):
        if (first_day + i) % 7 == weekday:
            if day == 1:
                return f'{i + 1} {cur_month} {year}'
            else:
                day -= 1
    else:
        raise WrongNumber(cur_month, cur_day, cur_weekday)





if __name__ == '__main__':
    print(extract_date_from_text('1-й четверг апреля'))
    print(check_date("1-й четверг апреля"))