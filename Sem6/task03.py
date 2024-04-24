def riddles(question: str, answers: list[str], tries: int) -> int:
    print(f'The puzzle is : "{question}".')
    for user_tries in range(1, tries + 1):
        user_answer = input('Enter your answer:\n')
        if user_answer.lower() in list(map(lambda x: x.lower(), answers)):
            return user_tries
        else:
            print(f"Wrong answer. You have {tries - user_tries} attempts left.")
    return 0


if __name__ == '__main__':
    riddle_ = 'зимой и летом одним цветом'
    answers_ = ['ёлка', 'ель', 'Сосна', 'туя', 'пихта']
    attempts_ = 3
    print(riddles(riddle_, answers_, attempts_))
