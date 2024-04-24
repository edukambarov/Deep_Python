# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
#
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
#
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# Пример
#
# На входе:
#
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# На выходе, например, один из допустимых вариантов может быть таким:
#
#
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
#
# max_weight = 1.0

items = {
    "спальник": 1.0,
    "палатка": 2.0,
    "термос": 0.5,
    "карта": 0.1,
    "фонарик": 0.2,
    "котелок": 0.5,
    "еда": 2.0,
    "одежда": 1.0,
    "обувь": 0.8,
    "нож": 0.2
}
max_weight = 8.2

backpack = dict()
b_weight = 0
min_rem = min(items.values())
while b_weight + min_rem <= max_weight:
    for k, v in items.copy().items():
        if v == min_rem:
            backpack[k] = items.pop(k)
            b_weight += v
            if len(items) > 0 and b_weight + min_rem <= max_weight:
                min_rem = min(items.values())
            else:
                break
print(b_weight)
print(max_weight - b_weight)


# backpack = {}
#
# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight

backpacks_test = []
sorted_result = []
for i in range(2 ** len(items)):
    backpack_test = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack_test[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks_test.append(backpack_test)

full_result = [backpack_test for backpack_test in backpacks_test if backpack_test]

result = []
for item in full_result:
    if item not in result:
        result.append(item)

x = 0
for i in result:
    if dict(sorted(i.items(), key=lambda item: item[1], reverse=True)) == dict(
            sorted(backpack.items(), key=lambda item: item[1], reverse=True)):
        x += 1

if x > 0:
    print(True)
else:
    print(False)

print(backpack)
print(sum(backpack.values()) <= max_weight)
print(items)

# Часто встречающиеся слова
#
# Инструкция по использованию платформы
#
#
#
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# Пример
#
# На входе:
#
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]


# text = "Python 3.9 is the latest version of Python. It's awesome!"
#
# punctuation_marks = ",;.'!?0123456789"
# for mark in punctuation_marks:
#     text = text.replace(mark,' ')
# text_spl = [x for x in text.lower().split(' ') if len(x) > 0]
# res = [(x, text_spl.count(x)) for x in list(set(text_spl))]
# res.sort(reverse=True)
# res.sort(key=lambda el: el[1], reverse=True)
# res = res[:10]
# print(res)
#
# print([('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)])


# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# Пример
#
# На входе:
#
#
# lst = [1, 1, 2, 2, 3, 3]
# На выходе:
#
#
# [1, 2, 3]


# lst = [1, 1, 2, 2, 3, 3, 4]
# print(list(set([x for x in lst if lst.count(x)>1])))


# адание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = 'А роза упала на лапу Азора'
d = {}
words = text.split()
letters = [char for word in text.lower().split() for char in word]
letters = [item for item in text.lower()]
for x in letters:
    d[x] = d.get(x,0)+1
print(d)


# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

f1 = 'Bob'
f2 = 'Tom'
f3 = 'Sam'
f1_things = ('thing1', 'thing2', 'thing6')
f2_things = ('thing1', 'thing2', 'thing3', 'thing4', 'thing5')
f3_things = ('thing2','thing3', 'thing4', 'thing7')
d = {}
d[f1] = f1_things
d[f2] = f2_things
d[f3] = f3_things
s1 = set(d[f1])
s2 = set(d[f2])
s3 = set(d[f3])
print(q1 := s1.intersection(s2).intersection(s3))
print(q2_1 := s1.difference(s2).difference(s3))
print(q2_2 := s2.difference(s1).difference(s3))
print(q2_3 := s3.difference(s2).difference(s1))
print(q3_1 := f'{f1, s2 & s3 - s1 if len(s2 & s3 - s1) > 0 else None}')
print(q3_2 := f'{f2, s1 & s3 - s2 if len(s1 & s3 - s2) > 0 else None}')
print(q3_3 := f'{f3, s1 & s2 - s3 if len(s1 & s2 - s3) > 0 else None}')


friends = {
'Максим': ('топор', 'вода', 'еда', 'палатка'),
'Шамиль': ('топор', 'вода', 'закуска', 'карты'),
'Сергей': ('топор', 'водка', 'еда', 'карты')
}

all_things = set()
for friend_item in friends.values():
    all_things.update(set(friend_item))

have_all_friends = all_things.copy()
for friend_item in friends.values():
    have_all_friends.intersection_update(friend_item)
print('Вещи, которые есть у всех:')
print(*have_all_friends)
print()

only_one_friend = {}
for friend in friends:
    friend_backpack = set(friends[friend])
    for other_friend in friends:
        if friend != other_friend:
            friend_backpack.difference_update(friends[other_friend])
        if friend_backpack:
            only_one_friend[friend] = friend_backpack
print('Есть только у одного:', *[f'{name}: {", ".join(back)}' for name, back in only_one_friend.items()], sep='\n')
print()

all_except_one_friend = {}
for friend in friends:
    friend_backpack = friends[friend]
    friends_backpacks = all_things.copy()
    for other_friend in friends:
        if friend != other_friend:
            friends_backpacks.intersection_update(friends[other_friend])
        friends_backpacks.difference_update(friend_backpack)
        if friends_backpacks:
            all_except_one_friend[friend] = friends_backpacks
print('Есть у всех, кроме одного:', *[f'{name} не взял: {", ".join(back)}' for name, back in all_except_one_friend.items()], sep='\n')