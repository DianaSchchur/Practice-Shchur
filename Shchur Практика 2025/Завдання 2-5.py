def palindrome(num):  # Функція для перевірки, чи є число паліндромом
    return str(num) == str(num)[::-1]  # Порівнюємо число з його оберненою версією

palindromes = []  # Список для збереження результатів

for number in range(1, 100):  # Перебираємо числа від 1 до 99
    if palindrome(number) and palindrome(number ** 2):  # Перевіряємо число та його квадрат
        palindromes.append(number)

print("Результат", palindromes) 
