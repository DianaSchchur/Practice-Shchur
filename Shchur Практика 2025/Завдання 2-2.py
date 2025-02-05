def pascal_triangle(n):
    triangle = []  # Список для збереження 
    for i in range(n):  # Цикл для створення рядків
        row = [1] * (i + 1)  # Кожен рядок починаєтся та закінчується на 1

        for j in range(1, i):  # Заповнюємо елементи рядка
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Додаємо рядок до трикутника

    return triangle  # Вертаємо трикутник

n = int(input("Скільки рядків побудувати? "))

triangle = pascal_triangle(n)  # Будуємо трикутник Паскаля

for row in triangle:
    print(row)
