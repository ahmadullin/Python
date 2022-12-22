from prettytable import PrettyTable

def log():
    log_table = PrettyTable()
    log_table.field_names = ['id', 'Имя', 'Фамилия','Номер телефона']
    return log_table
    
def path():
    file_path = r'C:\Users\1\Desktop\Python\Solving_tasks_7\call_log.txt'
    return file_path