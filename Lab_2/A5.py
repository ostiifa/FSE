a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
result = ["NO", "YES"][a % b == 0]
print(result)