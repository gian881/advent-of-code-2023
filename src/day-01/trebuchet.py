def main() -> None:
    with open('./input.txt', "r", encoding='utf-8') as file:
        text = file.read()
    soma = 0
    for line in text.split('\n'):
        primeiro: str = ""
        ultimo: str = ""
        current_index: int = 0
        for index in range(len(line)):
            if line[index].isdigit():
                primeiro = line[index]
                ultimo = line[index]
                break
            current_index = index
        for i in range(current_index, len(line)):
            if line[i].isdigit():
                ultimo = line[i]
        soma += int(primeiro + ultimo)
    print(soma)


if __name__ == "__main__":
    main()
