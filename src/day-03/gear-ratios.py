SYMBOLS: list[str] = ['@', '%', '&', '/', '+', '=', '#', '$', '*', '-']


def get_number_size(line: str, index: int) -> int:
    size = 0
    for i in range(index, len(line)):
        if line[i].isnumeric():
            size += 1
        else:
            break

    return size


def is_part_number(lines: list[str], line_index: int, number_start_index: int, number_end_index: int) -> bool:
    try:
        for char in lines[line_index-1][max(number_start_index-1, 0):min(number_end_index+1, len(lines[line_index-1])-1)]:
            if char in SYMBOLS:
                return True
    except IndexError:
        pass
    if lines[line_index][max(number_start_index-1, 0)] in SYMBOLS or lines[line_index][min(number_end_index, len(lines[line_index])-1)] in SYMBOLS:
        return True
    try:
        for char in lines[line_index+1][max(number_start_index-1, 0):min(number_end_index+1, len(lines[line_index+1])-1)]:
            if char in SYMBOLS:
                return True
    except IndexError:
        pass
    return False


def main() -> None:
    with open('./input.txt', 'r', encoding='utf-8') as file:
        lines: list[str] = file.readlines()

    sum = 0
    for line_index, line in enumerate(lines):
        char_index = 0
        while char_index < len(line):
            if line[char_index].isnumeric():
                size = get_number_size(line, char_index)
                if is_part_number(lines, line_index, char_index, char_index+size):
                    print(line[char_index:char_index+size])
                    sum += int(line[char_index:char_index+size])
                char_index += size
                continue
            char_index += 1

    print(sum)


if __name__ == "__main__":
    main()
