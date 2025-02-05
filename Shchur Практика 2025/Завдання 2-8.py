import textwrap

# Функція для форматування тексту із заданою шириною рядка
def format_text(text, n):
    # Перевірка значення n
    if n <= 50:
        print("Число n повинно бути більше 50.")
        return text
    
    # Розділяємо текст на абзаци
    paragraphs = text.split('\n\n')
    
    # Форматуємо кожен абзац із заданою шириною
    formatted_paragraphs = [textwrap.fill(paragraph.strip(), width=n) for paragraph in paragraphs]
    
    # Об'єднуємо абзаци із подвійним переносом рядка
    return '\n\n'.join(formatted_paragraphs)

try:
    # Введення тексту та ширини
    text = input("Введіть текст: ")
    n = int(input("Введіть ширину рядка (n > 50): "))
    
    formatted_text = format_text(text, n)
    print("\nВідформатований текст:\n")
    print(formatted_text)
except ValueError:
    print("Будь ласка, введіть правильне число.")
