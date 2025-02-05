import sys  # Для вихода при помилі
import math  # Для того щоб знайти корень

def gold_triangles(n):
    if n < 1:
        print("Число n повино бути більше за 0")
        sys.exit()  # Завершаем программу, если n некорректно
    
    return_value = []  # Список для збереження трійок

    # Перебираємо значення a і b
    for a in range(1, n): 
        for b in range(a, n):  # b починається з a, щоб не було дублікатів
            c = math.isqrt(a ** 2 + b ** 2)  # корень з суми
            if c < n and a ** 2 + b ** 2 == c ** 2:  # Перевірка цілого числа
                return_value.append((a, b, c))  # Добавляем подходящую тройку в список

    return return_value  # Вертаємо трійки
try:
    n = int(input("Введіть число n: "))
    result = gold_triangles(n)
    print("Знайдені трійки:", result)
except ValueError:
    print("Помилка: Введіть ціле число")
