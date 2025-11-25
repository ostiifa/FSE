def draw_rectangle(rows, columns, ch):
    """Функция для рисования прямоугольника"""
    print(f"\nПРЯМОУГОЛЬНИК {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    """Функция для рисования рамки"""
    print(f"\nРАМКА {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()

def draw_right_triangle(rows, ch):
    """Функция для рисования правого треугольника"""
    print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК ({rows} строк):")
    for i in range(rows):
        for j in range(i + 1):
            print(ch, end='')
        print()
print("РИСОВАНИЕ ФИГУР")
print("=" * 30)

try:
    n_rect = int(input("Введите количество строк для прямоугольника и рамки: "))
    m_rect = int(input("Введите количество столбцов для прямоугольника и рамки: "))
    n_triangle = int(input("Введите количество строк для треугольника: "))
    symbol = input("Введите символ для рисования (по умолчанию #): ") or '#'
except ValueError:
    print("Пожалуйста, введите целые числа!")
    exit()

draw_rectangle(n_rect, m_rect, symbol)
draw_frame(n_rect, m_rect, symbol)
draw_right_triangle(n_triangle, symbol)