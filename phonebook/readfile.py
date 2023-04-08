
def show_all():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    # print(data)
    file.close()
    # print(data[0])
    for i in data:
        print(i.split(';'))

def main_menu():
    print("Главное меню:")
    print('1. Показать весь справочник')
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск контакта")
    print("5. Удалить контакт")
    print("6. Вернуться в главное меню")
def add_contakt():
    file = open('sample.txt', 'a', encoding='UTF-8')
    data += '\n'
    data = input("Введите фамилию, телефон, комментарий (разделяя ;): ") #.split(';')
    data += '\n'
    file.write(data)
    file.close()
    # print("input data", data)

def find_contakt():
    find_string = input("Введите поисковый запрос: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for data_str in data:
        if find_string in data_str:
            print(data_str)
    file.close()

def edit_contakt():
     find_string = input("Введите поисковый запрос для изменения записи: ")
     replace_string = input("Введите новую строку справочника (разделяя ;): ")
     file = open('sample.txt', 'r', encoding='UTF-8')
     data = file.readlines()
     data_new = []
     for data_str in data:
         if find_string in data_str:
             data_new.append(replace_string)
         else:
             data_new.append(data_str)
     file.close()
     file = open('sample.txt', 'w', encoding='UTF-8')
     for row in data_new:
        file.write(row.__str__())
     file.close()


def del_contakt():
    find_string = input("Введите поисковый запрос для удаления записи: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    data_new = []
    for data_str in data:
        if find_string not in data_str:
            data_new.append(data_str)
    file.close()
    file = open('sample.txt', 'w', encoding='UTF-8')
    for row in data_new:
        file.write(row.__str__())
    file.close()






