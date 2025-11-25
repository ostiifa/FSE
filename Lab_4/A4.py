import re


def isValidNumber(string):
    """Функция 1: Проверка корректности введенного номера"""
    return string.isdigit() and len(string) in [13, 15, 16]


def getCheckSum(string):
    """Функция 2: Вычисление контрольной суммы по алгоритму Луна"""
    checkSum = 0
    for i in range(len(string) - 2, -1, -2):
        digit = int(string[i])
        doubled = digit * 2
        if doubled > 9:
            checkSum += 1 + (doubled - 10)
        else:
            checkSum += doubled
    for i in range(len(string) - 1, -1, -2):
        checkSum += int(string[i])

    return checkSum


def getCardType(string):
    """Функция 3: Определение типа карты"""
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid"

def main():
    cardNumber = input("Введите номер банковской карты: ").strip()

    if isValidNumber(cardNumber):
        if getCheckSum(cardNumber) % 10 == 0:
            card_type = getCardType(cardNumber)
            print(f"Карта действительна. Тип: {card_type}")
        else:
            print("Недействительный номер карты (ошибка контрольной суммы)")
    else:
        print("Неверный формат номера карты")

if __name__ == "__main__":
    main()