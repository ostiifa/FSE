x1 = int(input("Введите первую координату первой клетки "))
y1 = int(input("Введите вторую координату первой клетки "))
x2 = int(input("Введите первую координату второй клетки "))
y2 = int(input("Введите вторую координату второй клетки "))
color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2
if color1 == color2:
    print("YES")
    if color1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")