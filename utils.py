def inputsAsList(day: int):
    with open(f'inputs/day{day}.txt') as f:
        return f.read().splitlines()


def inputAsString(day: int):
    with open(f'inputs/day{day}.txt') as f:
        return f.read()
