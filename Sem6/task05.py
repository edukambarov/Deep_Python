from task03 import riddles
from random import choice


def play_puzzles(puzzles_data: dict[str: list[str]], count: int, attempts: int) -> str:
    result = []
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = riddles(puzzle, answers, attempts)
        result.append(f'Загадка "{puzzle}"' + (f' отгадана с {puzzle_count} попытки' if puzzle_count else
        ' не отгадана'))
        count -= 1
    return '\n'.join(result)


if __name__ == '__main__':
    puzzles = {'Ни лает, ни кусает, в дом не пускает?': ['замок', 'консьерж', 'дверь'],
               'Висит груша, нельзя скушать?': ['боксёрский мешок','лампочка', 'лампа'],
               'Зимой и летом одним цветом?': ['ёлка', 'ель', 'Сосна', 'туя', 'пихта']}

    print(play_puzzles(puzzles, 1, 3))