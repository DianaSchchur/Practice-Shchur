def sieve(limit):
    sieve = [True] * (limit + 1)  # Створюємо список, де всі числа спочатку вважаються простими
    sieve[0] = sieve[1] = False  # 0 і 1 не є простими числами
    
    for num in range(2, int(limit ** 0.5) + 1):  # Перебираємо числа від 2 до кореня з limit
        if sieve[num]:  # Якщо число не викреслене, воно просте
            for multiple in range(num * num, limit + 1, num):  # Викреслюємо всі його кратні
                sieve[multiple] = False
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]  # Збираємо всі прості числа
    return primes
primes = sieve(1000)
print("Решет Ератосфена", primes)  

