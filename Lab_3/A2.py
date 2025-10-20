import string
password = input()
errors = []
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")
if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")
special_chars = "*-#"
if not any(symbol in special_chars for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")
allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
for symbol in password:
    if symbol not in allowed_chars:
        errors.append("В пароле используются непредусмотренные символы")
        break
if not errors:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)