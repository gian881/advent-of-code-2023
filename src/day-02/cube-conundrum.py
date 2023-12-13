from dataclasses import dataclass
quantities = {
    'red': 12,
    'green': 13,
    'blue': 14
}


@dataclass
class SetOfResult:
    quantity: int
    color: str


class Game:
    id: int
    sets: list[SetOfResult]

    def __init__(self, id: int, sets: list[SetOfResult]) -> None:
        self.id = id
        self.sets = sets


def get_sets_of_results(line: str) -> list[SetOfResult]:
    sets_of_results: list[SetOfResult] = []

    results: list[str] = [result for result in line.split(':')[1].split(";")]
    for result in results:
        hm: list[str] = result.split(',')
        for coisa in hm:
            quantity, color = coisa.strip().split(" ")
            sets_of_results.append(SetOfResult(int(quantity), color))
    return sets_of_results


def get_game_id(line: str) -> int:
    return int(line.split(":")[0].split(" ")[1])


def is_possible(set: SetOfResult):
    return set.quantity <= quantities.get(set.color, -1)


def main() -> None:
    with open('./input.txt', "r", encoding='utf-8') as file:
        text = file.read()
    games = [Game(get_game_id(line), get_sets_of_results(line))
             for line in text.splitlines()]
    sum = 0
    for game in games:
        possible = True
        for set in game.sets:
            if not is_possible(set):
                possible = False
                break
        if possible:
            sum += game.id
    print(sum)


if __name__ == "__main__":
    main()
