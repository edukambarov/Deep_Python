from task03 import riddles
from random import choice


_dict_answers = {}

def play_puzzles(puzzles_data: dict[str: list[str]], count: int, attempts: int):
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = riddles(puzzle, answers, attempts)
        _dict_answers[puzzle] = f'Отгадана с {puzzle_count} попытки.' \
            if puzzle_count else 'Не отгадана.'
        count -= 1


def print_protected_dict():
    for puzzle, answer in _dict_answers.items():
        print(f'Загадка: {puzzle}\n{answer}')


if __name__ == '__main__':
    puzzles = {'Ни лает, ни кусает, в дом не пускает?': ['замок', 'консьерж', 'дверь'],
               'Висит груша, нельзя скушать?': ['боксёрский мешок','лампочка', 'лампа'],
               'Зимой и летом одним цветом?': ['ёлка', 'ель', 'Сосна', 'туя', 'пихта']}

    play_puzzles(puzzles, 2, 3)
    print_protected_dict()