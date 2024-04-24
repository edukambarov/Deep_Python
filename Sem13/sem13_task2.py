# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений

def get(dictionary,key,default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default


if __name__ == '__main__':
    data_dict = {1:'one', 2:'two'}
    key = 1
    data_dict = get(data_dict,key)
    print(f'Значение для ключа "{key}": {data_dict}')