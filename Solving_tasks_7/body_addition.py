import table_create as table

file_path = table.path()
log_table = table.log()

def call_log_addition(k):
    count = 0
    with open (file_path, 'r') as f_data:
        for i in f_data.readlines():
            i = i.replace('\n','')
            i = i.split(' ')
            if k[2] == i[3]:
                count += 1
                log_table.add_row(i)
    
    if count > 0: print (f'Такой контакт уже существует\n{log_table}')
    
    if count == 0:
        with open (file_path, 'r') as f_data:
            a = len(f_data.readlines())
            with open (file_path, 'a') as f_data:
                if a == 0: f_data.write(f'{a+1} {k[0]} {k[1]} {k[2]}')
                else: f_data.write(f'\n{a+1} {k[0]} {k[1]} {k[2]}')
        with open (file_path, 'r') as f_data:
            for i in f_data.readlines():
                count += 1
                log_table.add_row(i.split(' '))
        print(log_table)