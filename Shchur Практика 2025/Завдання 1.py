def analyze_string():
    input_string = input("Введите строку: ")

    vowels = "аоуеиіАОУЕІИaeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРОТФХЦЧШЩ"
    
    # Сортируем гласные в обратном алфавитном порядке
    vowels_in_string = sorted([char for char in input_string if char in vowels], reverse=True)
    # Сортируем согласные в обратном алфавитном порядке
    consonants_in_string = sorted([char for char in input_string if char in consonants], reverse=True)
    
    # Проверяем, больше ли 3 согласных
    has_more_than_three_consonants = len(consonants_in_string) > 3

    return ("".join(vowels_in_string), has_more_than_three_consonants, "".join(consonants_in_string))

# Вызываем функцию и печатаем результат
result = analyze_string()
print(result)
