from import_data import import_data
from export_data import export_data
from print_data import print_data

def greeting():
    print("Вы открыли телефонный справочник")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    contact_description = input("опишите контакт: ")
    return [last_name, first_name, phone_number, contact_description]

def choice_separator():
    separator = input("Есть 2 варианта записи. Введите разделитель: ")
    if separator == "":
        separator = None
    return separator

def phone_book_functionality():
    print("Что вы можете сделать:\n\
    1 - добавление контакта;\n\
    2 - вывод контакта.")
    choice = input(" Что вы хотите сделать - введите цифру: ")
    if choice == '1':
        separator = choice_separator()
        import_data(input_data(), separator)
    elif choice == '2':
        separator = choice_separator()
        export_data(separator)
        data = export_data(separator)
        print_data(data, separator)
   