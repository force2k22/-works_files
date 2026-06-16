def search_word():
    search_word_input = input("напиши слово ").lower()

    with open('resource/text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    count = 0
    found_lines = []

    for i, line in enumerate(lines, 1):
        if search_word_input in line.lower():
            count += line.lower().count(search_word_input)
            found_lines.append(i)

    result = f"слово: {search_word_input}\n"
    result += f"нашлось: {'да' if count > 0 else 'нет'}\n"
    result += f"кол во: {count}\n"
    result += f"строки: {found_lines}\n"

    with open('resource/search_results.txt', 'w', encoding='utf-8') as file:
        file.write(result)

    print("\n" + result)
    print("Результаты соранены в папки resource/search_results.txt")


if __name__ == "__main__":
    search_word()