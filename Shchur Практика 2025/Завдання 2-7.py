def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Пошук пар простих чисел із різницею 2 у діапазоні від n до 2n
def find_prime_pairs(n):
    pairs = []
    for x in range(n, 2 * n - 1):
        if prime(x) and prime(x + 2):
            pairs.append((x, x + 2))

    return pairs

try:
    n = int(input("Введіть число n (n > 1): "))
    if n > 1:
        result = find_prime_pairs(n)
        if result:
            print("Пари простих чисел із різницею 2:")
            for pair in result:
                print(pair)
        else:
            print("Не знайдено жодної пари.")
    else:
        print("Число повинно бути більше 1.")
except ValueError:
    print("Будь ласка, введіть ціле число.")
