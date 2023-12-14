from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    line: int
    column: int


@dataclass(frozen=True)
class Number:
    start: Coordinate
    end: Coordinate


def find_start_and_end_index(lines: list[str], line_index: int, index: int) -> Number:
    start_index: int = index
    end_index: int = index
    for i in range(index, -1, -1):
        if lines[line_index][i].isnumeric():
            start_index = i
        else:
            break
    for i in range(index, len(lines[line_index])):
        if lines[line_index][i].isnumeric():
            end_index = i
        else:
            break
    return Number(Coordinate(line_index, start_index), Coordinate(line_index, end_index))


def find_numbers_around_gear(lines: list[str], line_index: int, gear_index: int) -> list[tuple[int, int]]:
    numbers_coordinates: list[tuple[int, int]] = []
    for i in range(gear_index-1, gear_index+2):
        if lines[line_index-1][i].isnumeric():
            numbers_coordinates.append((line_index-1, i))
        if lines[line_index+1][i].isnumeric():
            numbers_coordinates.append((line_index+1, i))
    if lines[line_index][gear_index-1].isnumeric():
        numbers_coordinates.append((line_index, gear_index-1))
    if lines[line_index][gear_index+1].isnumeric():
        numbers_coordinates.append((line_index, gear_index+1))
    return numbers_coordinates


def main() -> None:
    with open('./input.txt', 'r', encoding='utf-8') as file:
        lines: list[str] = file.readlines()

    sum = 0
    for line_index, line in enumerate(lines):
        char_index = 0
        while char_index < len(line):
            if line[char_index] == '*':
                numbers: set[Number] = set()
                for l_index, c_index in find_numbers_around_gear(lines, line_index, char_index):
                    number: Number = find_start_and_end_index(
                        lines, l_index, c_index)
                    numbers.add(number)

                if len(numbers) == 2:
                    numbers_list = list(numbers)
                    number1 = int(lines[numbers_list[0].start.line]
                                  [numbers_list[0].start.column:numbers_list[0].end.column+1])
                    number2 = int(lines[numbers_list[1].start.line]
                                  [numbers_list[1].start.column:numbers_list[1].end.column+1])
                    sum += number1 * number2
            char_index += 1
    print(sum)


if __name__ == "__main__":
    main()
