import random
import time
try:
    N = int(input("Введите количество примеров: "))
except ValueError:
    print("Пожалуйста, введите целое число!")
    exit()
correct_answers = 0
total_time = 0
question_times = []

print()
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b
    while True:
        try:
            start_time = time.time()
            user_answer = int(input(f"Вопрос {i + 1}/{N}\n{a} × {b} = "))
            time_spent = time.time() - start_time
            total_time += time_spent
            question_times.append(time_spent)
            if user_answer == correct_result:
                print(f"Верно! (Время: {time_spent:.1f} сек)")
                correct_answers += 1
            else:
                print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")

            break

        except ValueErroR:
            print("Пожалуйста, введите целое число!")
print("\n" + "=" * 40)
print("СТАТИСТИКА:")
print("=" * 40)
print(f"Общее время: {total_time:.1f} секунд")

if N > 0:
    average_time = total_time / N
    print(f"Среднее время на вопрос: {average_time:.1f} сек")

print(f"Правильных ответов: {correct_answers}/{N}")

if N > 0:
    percentage = (correct_answers / N) * 100
    print(f"Процент правильных: {percentage:.1f}%")