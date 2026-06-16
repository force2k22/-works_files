def count_lines_and_words():
    with open('resource/input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)

    with open('resource/statistics.txt', 'w', encoding='utf-8') as file:
        file.write(f"трок: {num_lines}\n")
        file.write(f"слов: {num_words}\n")

    print(f"трок: {num_lines}")
    print(f"слов: {num_words}")
    print("Results saved to resource/statistics.txt")


if __name__ == "__main__":
    count_lines_and_words()