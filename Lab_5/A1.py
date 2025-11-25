def shorten_text(text):
    while True:
        left_bracket = text.find('(')
        right_bracket = text.find(')')

        if left_bracket == -1 or right_bracket == -1:
            break

        text = text.replace(text[left_bracket:right_bracket + 1], '')

    text = ' '.join(text.split())
    return text
print("Введите текст (содержащий круглые скобки):")
user_text = input()
result_text = shorten_text(user_text)
print("\nУкороченный текст:")
print(result_text)