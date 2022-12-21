import table_create as table
import view

file_path = table.path()
log_table = table.log()

def call_log_search(contact):
    count = 0
    with open (file_path, 'r') as f_data:
        for i in f_data.readlines():
            i = i.replace('\n','')
            i = i.split(' ')
            for j in i:
                if contact == j:
                    count += 1
                    log_table.add_row(i)
        if count == 0: print('Такого контакта нет. Проверьте правильно ли вы ввели данные')
        if count == 1: print (log_table)
        if count > 1:
            print (log_table)
            num = view.interview_search_2()
            table = log_table.get_string(start = num - 1, end = num)
            print (table)