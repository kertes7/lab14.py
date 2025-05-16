import os

FILENAME = "travel_notes.txt"

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', encoding='utf-8') as file:
            file.write("Щоденник мандрівника\n\n")

    while True:
        print("\nЩоденник мандрівника")
        print("1. Додати новий запис")
        print("2. Пошук записів")
        print("3. Статистика")
        print("4. Вийти")
        
        choice = input("Виберіть опцію (1-4): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            search_entries()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def add_entry():
    print("\nДодавання нового запису:")
    date = input("Введіть дату (РРРР-ММ-ДД): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст нотатки: ")
    
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("-" * 40 + "\n")
    print("Запис успішно додано!\n")

def search_entries():
    print("\nПошук записів:")
    print("1. По даті")
    print("2. По ключовому слову")
    choice = input("Виберіть опцію (1/2): ")
    
    with open(FILENAME, 'r', encoding='utf-8') as file:
        entries = file.read().split('-' * 40 + '\n')[:-1]
    
    found_entries = []
    if choice == '1':
        search_date = input("Введіть дату для пошуку (РРРР-ММ-ДД): ")
        for entry in entries:
            if f"Дата: {search_date}" in entry:
                found_entries.append(entry)
    elif choice == '2':
        keyword = input("Введіть ключове слово для пошуку: ")
        for entry in entries:
            if keyword.lower() in entry.lower():
                found_entries.append(entry)
    
    if found_entries:
        print("\nЗнайдені записи:")
        for entry in found_entries:
            print(entry)
            print('-' * 40)
    else:
        print("Записи не знайдено.")

def show_statistics():
    with open(FILENAME, 'r', encoding='utf-8') as file:
        content = file.read()
    
    entries = content.split('-' * 40 + '\n')[:-1]
    locations = set()
    word_count = 0
    
    for entry in entries:
        lines = entry.split('\n')
        for line in lines:
            if line.startswith("Локація:"):
                location = line.split(": ")[1].strip()
                locations.add(location)
            elif line.startswith("Текст:"):
                text = line.split(": ")[1]
                word_count += len(text.split())
    
    print("\nСтатистика:")
    print(f"Кількість записів: {len(entries)}")
    print(f"Кількість унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів у нотатках: {word_count}")

if __name__ == "__main__":
    main()
