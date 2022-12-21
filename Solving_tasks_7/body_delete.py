import table_create as table

file_path = table.path()

def call_log_delete(id):
    with open (file_path, 'r') as f_data:
        full = f_data.readlines()
        full.pop(id - 1)
    
    full_help = []
    for i in range(len(full)):
        z = full[i].split(' ')
        z[0] = f'{i + 1}'
        full_help.append(z)
    
    with open (file_path, 'w') as f_data:
        for i in range(len(full_help)):
            full_help[i] = ' '.join(full_help[i])

            if i != int(len(full_help) - 1):
                if '\n' not in full_help[i]: f_data.writelines(f'{full_help[i]}\n')
                else: f_data.writelines(f'{full_help[i]}')
            else:
                if '\n' not in full_help[i]: f_data.writelines(f'{full_help[i]}')
                else: f_data.writelines(f'{full_help[i]}')