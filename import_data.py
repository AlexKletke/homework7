# модуль Добавление контакта
 
"""def import_data(data, separator = None):
    with open('phone_book.csv', 'a+') as file:
        if separator == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(separator.join(data))
            file.write(f"\n")"""

def import_data(data, separator):
    if separator == None:
        with open('phone_book1.csv', 'a+') as file1:
            file1.write(f"{data[0]}\n")
            file1.write(f"{data[1]}\n")
            file1.write(f"{data[2]}\n")
            file1.write(f"{data[3]}\n")
            """for i in data:
                file1.write(f"{i[0]}\n")
                file1.write(f"{i[1]}\n")
                file1.write(f"{i[2]}\n")
                file1.write(f"{i[3]}\n")"""
            file1.write(f"\n")
    else:
        with open('phone_book2.csv', 'a+') as file2:
            file2.write(separator.join(data))
            file2.write(f"\n")