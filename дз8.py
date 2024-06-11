def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_sub(phone_book, last_name, 0))
        elif choice == 3:
            tel_number = input('Введите номер телефона: ')
            print(find_by_sub(phone_book, tel_number, 2))
        elif choice == 4:
            sub_data = []
            fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
            for i in range(0, 4):
                sub_data.append(str(input(f'{fields[i]}')))
            phone_book.append(add_new_sub(sub_data, phone_book))
            write_txt('phon.txt', phone_book)
            print(phone_book)
        elif choice == 5:
            choice = go_out()
        choice = show_menu()

def find_by_sub(phone_book, value, flag):
    if flag == 0:
        print('Поиск по фамилии')
    else:
        print('Поиск по номеру')
    for i in range(0, len(phone_book)):
        if [m for m in phone_book[i].values()][flag] == value:
            res = '___________\n'
            for teg1, teg2 in phone_book[i].items():
                res = f'{res}{teg1}:{teg2}\n'
            res = f'{res}___________\n'
    if res == '':
        res = 'Абонент не найден \n'
    return res

def go_out():
    print('Закончили работу')
    return 7

def add_new_sub(sub_data, phone_book):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, sub_data))
    phone_book.append(record)
    return phone_book

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            line = line.replace("\n", "")
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

work_with_phonebook()