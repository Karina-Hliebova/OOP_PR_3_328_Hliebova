# circle_module.py 

def CircleS(R):
    if not isinstance(R, (int, float)):
        raise TypeError("R має бути числом.")
    if R < 0:
        raise ValueError("Радіус не може бути від’ємним.")
    PI = 3.14
    return PI * R ** 2

def CircleS_list(r_list):
    return [CircleS(R) for R in r_list]


# task_circle.py

from circle_module import CircleS_list

def task_circle():
    """Введення даних, виклик функцій, виведення результатів."""
    try:
        r_list = [float(x) for x in input("Введіть три радіуси через пробіл: ").split()]
        if len(r_list) != 3:
            raise ValueError("Потрібно ввести рівно три радіуси!")

        s_list = CircleS_list(r_list)
        print("Радіуси:", r_list)
        print("Площі кіл:", s_list)

    except ValueError as e:
        print("Помилка введення:", e)
    except TypeError as e:
        print("Помилка типу:", e)


import numpy as np
import os

def task_matrix18():
    """Matrix18: знайти кількість стовпців з різними елементами
    і додати x випадкових рядків. Працює і в програмі на пристрої, і онлайн."""

    def matrix18_process(data):
        """Приймає NumPy-масив. Повертає кількість унікальних стовпців і нову матрицю."""
        M, N = data.shape
        count_unique_cols = sum(len(np.unique(data[:, j])) == M for j in range(N))
        random_rows = np.random.randint(-10, 11, size=(M, N))
        new_matrix = np.vstack((data, random_rows))
        return count_unique_cols, new_matrix

    # --- Перевіряємо, чи існує файл ---
    filename = "Matrix18.txt"
    data = None
    if os.path.exists(filename):
        try:
            data = np.loadtxt(filename, dtype=int)
            print(f"Матриця прочитана з файлу '{filename}':\n{data}")
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")

    # --- Якщо файлу немає, пропонуємо вибір ---
    if data is None:
        print("\nФайл 'Matrix18.txt' не знайдено або не може бути прочитаний.")
        print("Введіть 1, щоб ввести матрицю вручну.")
        print("Введіть 2, щоб використати стандартну матрицю (приклад).")
        mode = input("Ваш вибір (1 або 2): ").strip()

        if mode == "1":
            try:
                M = int(input("Введіть кількість рядків M: "))
                N = int(input("Введіть кількість стовпців N: "))
                print(f"Введіть матрицю ({M} рядків по {N} чисел у кожному):")
                rows = [list(map(int, input().split())) for _ in range(M)]
                data = np.array(rows)
            except Exception as e:
                print("Помилка введення. Використовується матриця за замовчуванням.")
                data = np.array([[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12]])
        else:
            print("Використовується матриця за замовчуванням:")
            data = np.array([[1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12]])
            print(data)

    # --- Обробка матриці ---
    count, new_matrix = matrix18_process(data)
    print(f"\nКількість стовпців, де всі елементи різні: {count}")
    print("\nНова матриця після додавання випадкових рядків:")
    print(new_matrix)

    # --- Спроба зберегти у файл (може не працювати в Online Python) ---
    try:
        np.savetxt("matrix18_result.txt", new_matrix, fmt="%d")
        print("\nРезультат збережено у файл 'matrix18_result.txt'.")
    except Exception:
        print("\n Онлайн-середовище не дозволяє зберігати файл — пропускаємо збереження.")


#script-file

main.py

from task_circle import task_circle
from task_matrix18 import task_matrix18

print("1 - Обчислити площі трьох кіл (Proc18)")
print("2 - Обробити матрицю (Matrix18)")
choice = input("Виберіть задачу (1 або 2): ")

if choice == "1":
    task_circle()
elif choice == "2":
    task_matrix18()
else:
    print("Невірний вибір.")
