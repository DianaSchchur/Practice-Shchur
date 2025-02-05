# Просте меню для керування бібліотекою
library_books = []

def display_books():
    """Виведення списку книг."""
    if library_books:
        print("\nСписок книг у бібліотеці:")
        for idx, book in enumerate(library_books, start=1):
            print(f"{idx}. {book}")
    else:
        print("\nБібліотека порожня.")

def add_book():
    """Додавання книги до списку."""
    book_name = input("Введіть назву книги: ").strip()
    if book_name:
        library_books.append(book_name)
        print(f"Книга '{book_name}' успішно додана!")
    else:
        print("Назва книги не може бути порожньою.")

def remove_book():
    """Видалення книги зі списку."""
    display_books()
    try:
        book_num = int(input("\nВведіть номер книги для видалення: "))
        if 1 <= book_num <= len(library_books):
            removed_book = library_books.pop(book_num - 1)
            print(f"Книга '{removed_book}' видалена.")
        else:
            print("Некоректний номер книги.")
    except ValueError:
        print("Будь ласка, введіть числове значення.")

def main():
    """Основне меню програми."""
    while True:
        print("\nМеню:")
        print("1. Показати список книг")
        print("2. Додати книгу")
        print("3. Видалити книгу")
        print("4. Вийти")
        
        choice = input("Оберіть дію (1-4): ")
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
