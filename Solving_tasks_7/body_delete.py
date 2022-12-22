import table_create as table

file_path = table.path()

def call_log_delete(id):
    with open (file_path, 'r') as f_data:
        full = f_data.readlines()
        full.pop(int(id) - 1)
    
    full_help = []
    for i in range(len(full)):
        z = full[i].split(' ')
        z[0] = f'{i + 1}'
        full_help.append(z)
    
    with open (file_path, 'w') as f_data:
        for i in range(len(full_help)):
            full_help[i] = ' '.join(full_help[i])

            if i != int(len(full_help) - 1):
                f_data.writelines(f'{full_help[i]}')
            else:
                full_help[i] = full_help[i].replace("\n","")
                f_data.writelines(f'{full_help[i]}')