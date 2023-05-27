'''Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.'''

phone_book = {}

def add_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    phone_book[name] = phone
    print("Контакт добавлен.")

def update_contact():
    name = input("Введите имя контакта для изменения: ")
    if name in phone_book:
        new_phone = input("Введите новый номер телефона: ")
        phone_book[name] = new_phone
        print("Контакт обновлен.")
    else:
        print("Контакт не найден.")

def delete_contact():
    name = input("Введите имя контакта для удаления: ")
    if name in phone_book:
        del phone_book[name]
        print("Контакт удален.")
    else:
        print("Контакт не найден.")

def search_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phone_book:
        print("Номер телефона:", phone_book[name])
    else:
        print("Контакт не найден.")
while True:
    print("\nТелефонный справочник")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4. Найти контакт")
    print("5. Выйти")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")