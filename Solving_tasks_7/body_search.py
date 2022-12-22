import table_create as table
import body_delete as delete
import body_change as change
import view

file_path = table.path()
log_table = table.log()
x = table.log()

def call_log_search(contact):
    count = 0
    with open (file_path, 'r') as f_data:
        for i in f_data.readlines():
            i = i.replace('\n','').split(' ')
            for j in i:
                if contact == j:
                    count += 1
                    num = int (i[0])
                    log_table.add_row(i)
                    
        if count == 0: print('Такого контакта нет. Проверьте правильно ли вы ввели данные')
        if count == 1: print (log_table)
        if count > 1:
            print (log_table)
            num = f'{view.interview_search_2()}'
            with open (file_path, 'r') as f_data:
                for i in f_data.readlines():
                    if num == i[0]:
                        x.add_row(i.split(' '))
                print(f'\n {x}')

        if count > 0:
            k = view.interview_change_1()

            if k == 1:
                change.call_log_change(num, view.interview_change_2())

            if k == 2:
                delete.call_log_delete(num)               