digits: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_digit_from_spelled_out_number(line, index, end) -> str:
    return digits.get(line[index:end], "1")


def is_spelled_out_number(line: str, index: int) -> tuple[bool, int]:
    if line[index] not in ['o', 't', 'f', 's', 'e', 'n']:
        return False, -1
    try:
        if line[index:index+3] in ["one", "two", "six"]:
            return True, index + 3
        elif line[index:index+4] in ["four", "five", "nine"]:
            return True, index + 4
        elif line[index:index+5] in ["three", "seven", "eight"]:
            return True, index + 5
        else:
            return False, -1
    except IndexError:
        return False, -1


def main() -> None:
    with open('./01-input.txt', "r", encoding='utf-8') as file:
        text: str = file.read()
    sum = 0
    for line in text.split('\n'):
        first: str = ""
        last: str = ""
        index: int = 0
        while index < len(line):
            if line[index].isdigit():
                first = line[index]
                last = line[index]
                break
            is_number_spelled_out, end = is_spelled_out_number(line, index)
            if is_number_spelled_out:
                first = get_digit_from_spelled_out_number(
                    line, index, end)
                last = get_digit_from_spelled_out_number(
                    line, index, end)
                index = index + 1
                break
            index += 1
        while index < len(line):
            if line[index].isdigit():
                last = line[index]
            is_number_spelled_out, end = is_spelled_out_number(line, index)
            if is_number_spelled_out:
                last = get_digit_from_spelled_out_number(
                    line, index, end)
                index = index + 1
                continue
            index += 1
        sum += int(first + last)
    print(sum)


if __name__ == "__main__":
    main()
