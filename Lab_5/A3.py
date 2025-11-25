def create_abbreviation(text):
    words = text.split()
    abbreviation = ''
    for word in words:
        if len(word) >= 3:
            abbreviation += word[0].upper()

    return abbreviation
print("Введите текст:")
text = input()
abbrev = create_abbreviation(text)
print(f"Вывод: {abbrev}")