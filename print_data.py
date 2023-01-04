"""def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
        print("-"*130)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
    else:
        print("Телефонный справочник пустой")"""

def print_data(data, separator):
    if separator == None:
        print(f"Фамилия: {data[0]}\n Имя: {data[1]}\n Телефон: {data[2]}\n Описание: {data[3]}")
    else:
        for item in data:
            print(f"Фамилия: {item[0]}, Имя: {item[1]}, Телефон: {item[2]}, Описание: {item[3]}")