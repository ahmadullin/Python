import table_create as table

file_path = table.path()
log_table = table.log()

def call_log_all():
    count = 0
    with open (file_path, 'r') as f_data:
        for i in f_data.readlines():
            count += 1
            log_table.add_row(i.split(' '))

        if count > 0: print (log_table)
        if count == 0: print('Телефонный справочник пуст')