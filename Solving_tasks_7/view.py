num_1 = 0

contact = ''

id = 0

name = ''
surname = ''
number = ''

num_2 = 0

num_3 = 0

# main
def interview_main():
    global num_1
    print('\n Телефонный справочник\n')
    num_1 = int(input('Что необходимо сдеть?\n 1 - Посмотреть все контакты\n 2 - Найти контакт\n 3 - Добавить контакт\n\n Введите цифру --> '))
    return num_1


# search
def interview_search_1():
    global contact
    print('\n\n Телефонный справочник. Поиск контакта\n')
    contact = input('Введите имя или фамилию --> ')
    return contact

def interview_search_2():
    global id
    id = int (input('Выберите id нужного контакта --> '))
    return id


# change
def interview_change_1():
    global num_2
    num_2 = int(input('Что необходимо сдеть?\n 1 - Изменить контакт\n 2 - Удалить контакт\n\n Введите цифру --> '))
    return num_2

def interview_change_2():
    global num_3
    num_3 = int(input('Что необходимо изменить?\n 1 - Имя\n 2 - Фамилию\n 3 - Номер телефона\n\n Введите цифру --> '))
    return num_3

def interview_change_2_name():
    while (name := input('\n Введите имя --> ')) == '':
        print ('Вы ничего не ввели')
    return name
def interview_change_2_surname():
    while (surname := input('\n Введите фамилию --> ')) == '':
        print ('Вы ничего не ввели')
    return surname
def interview_change_2_number():
    while (number := (input('\n Введите номер телефона --> '))).isdigit() == False:
        print ('Вы ничего не ввели')
    return number


# addition
def interview_addition():
    global name, surname, number
    print('\n\n Телефонный справочник. Добавление контакта\n')
    while (name := input('\n Введите имя --> ')) == '':
        print ('Вы ничего не ввели')
    while (surname := input('\n Введите фамилию --> ')) == '':
        print ('Вы ничего не ввели')
    while (number := input('\n Введите номер телефона --> ')).isdigit() == False:
        print ('Вы ничего не ввели')
    return name, surname, number 