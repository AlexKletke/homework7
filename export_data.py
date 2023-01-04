# модуль Вывод контакта 

def export_data(separator):
    if separator == None:
        with open('phone_book1.csv', 'r') as file1:
            data1 = []
            for line in file1:
                if line != '\n':
                    data1.append(line.strip())
                data = data1
    else:
        with open('phone_book2.csv', 'r') as file2:
            data2 = []
        # t = []
            for line in file2:
                if ',' in line:
                # temp = line.strip().split(',')
                    temp = line.split(',')
                    data2.append(temp)
                elif ';' in line:
                    temp = line.split(';')
                    data2.append(temp)
                elif '-' in line:
                    temp = line.split('-')
                    data2.append(temp)
                elif '*' in line:
                    temp = line.split('*')
                    data2.append(temp)
                data = data2        
            """elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []"""
    return data