import table_create as table
import view

file_path = table.path()
log_table = table.log()

def call_log_change(id, action):
    with open (file_path, 'r') as f_data:
        full = f_data.readlines()
        z = full[id - 1].split(' ')
    if action == 1:
        z[1] = view.interview_change_2_name()
        z = " ".join(z)
    if action == 2:
        z[2] = view.interview_change_2_surname()
        z = " ".join(z)
    if action == 3:
        z[3] = view.interview_change_2_number()
        z = " ".join(z)
    
    full[id - 1] = z
    with open (file_path, 'w') as f_data:
        for i in range(len(full)):

            if i != int(len(full) - 1):
                if '\n' not in full[i]: f_data.writelines(f'{full[i]}\n')

            else:
                if '\n' not in full[i]: f_data.writelines(f'{full[i]}')