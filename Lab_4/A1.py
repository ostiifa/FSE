import random
import time


def multiplication_trainer():
    while True:
        try:
            n = int(input("Введите количество примеров: "))
            if n > 0:
                break
            else:
                print("Количество примеров должно быть положительным числом!")
        except ValueError:
            print("Пожалуйста, введите целое число!")

    correct_answers = 0
    total_time = 0
    question_times = []

    print("-" * 40)

    for i in range(1, n + 1):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        correct_result = a * b

        print(f"Вопрос {i}/{n}")

        while True:
            start_time = time.time()

            try:
                user_answer = input(f"{a} × {b} = ")
                end_time = time.time()

                time_spent = end_time - start_time
                user_answer_int = int(user_answer)

                if user_answer_int == correct_result:
                    print(f"Верно! (Время: {time_spent:.1f} сек)")
                    correct_answers += 1
                else:
                    print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")

                total_time += time_spent
                question_times.append(time_spent)
                break

            except ValueError:
                print("Пожалуйста, введите целое число!")

    print("-" * 40)
    print("СТАТИСТИКА:")
    print(f"Общее время: {total_time:.1f} секунд")

    if n > 0:
        average_time = total_time / n
        percentage = (correct_answers / n) * 100
        print(f"Среднее время на вопрос: {average_time:.1f} сек")
        print(f"Правильных ответов: {correct_answers}/{n}")
        print(f"Процент правильных: {percentage:.1f}%")

    print("-" * 40)

if __name__ == "__main__":
    multiplication_trainer()