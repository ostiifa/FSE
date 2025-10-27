def draw_rectangle(n, m, ch="#"):
    """Рисует прямоугольник размером n x m"""
    print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
    for i in range(n):
        for j in range(m):
            print(ch, end="")
        print()


def draw_right_triangle(n, ch="#"):
    """Рисует правый треугольник из n строк"""
    print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК ({n} строк):")
    for i in range(1, n + 1):
        for j in range(i):
            print(ch, end="")
        print()


def draw_frame(n, m, ch="#"):
    """Рисует рамку размером n x m"""
    print(f"\nРАМКА {n}x{m}:")
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()

def main():
    try:
        n = int(input("Введите количество строк (n): "))
        m = int(input("Введите количество столбцов (m): "))

        if n <= 0 or m <= 0:
            print("Размеры должны быть положительными числами!")
            return
        draw_rectangle(n, m)
        draw_right_triangle(n)
        draw_frame(n, m)

    except ValueError:
        print("Пожалуйста, введите целые числа!")
if __name__ == "__main__":
    main()