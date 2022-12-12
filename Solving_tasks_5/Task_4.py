# Модуль сжатия и восстановления данны

import os

# Сжатие файла

input_case = input ("Введите предложение: ")

if ' ' in (input_case):
    a = input_case.split(' ')
else:
    a = [input_case]

def сompress(x, count = 1):
    for i in range(len(x)):

        if i < (len(x) - 1):

            if x[i] == x[i+1]:
                count += 1
            
            else:

                if count > 1:
                    with open (file_path_1, 'a') as data:
                        data.write (f'{count}{x[i]}')
                    
                if count == 1:
                    with open (file_path_1, 'a') as data:
                        data.write (f'{x[i]}')

                count = 1

        if (i == (len(x)-1)) and (x[i] != x[i-1]):
            with open (file_path_1, 'a') as data:
                data.write (f'{x[i]}')

        if (i == (len(x)-1)) and (x[i] == x[i-1]):
            with open (file_path_1, 'a') as data:
                data.write (f'{count}{x[i]}')    

file_path_1 = r"C:\Users\1\Desktop\Python\Solving_tasks_5\Task_4_сжатый.txt"

for i in range(len(a)):
    if i < int (len(a) - 1):
        сompress(a[i])
        with open (file_path_1, 'a') as data:
            data.write (' ')
    if i == int (len(a) - 1):
        сompress(a[i])

with open (file_path_1, 'r') as data:
    print(f"Что в сжатом файле: {data.readline()}")


# Разжатие файла


with open (file_path_1, 'r') as data:
    b = data.readline()

os.remove(file_path_1)

if ' ' in (b):
    b = b.split(' ')
else:
    b = [b]

file_path_2 = r"C:\Users\1\Desktop\Python\Solving_tasks_5\Task_4_несжатый.txt"

def uncompress(p):
    for i in range(len(p)):
        if p[i].isdigit():
            with open (file_path_2, 'a') as data_f:
                data_f.write (f'{p[i+1]}')
        if not p[i].isdigit():
            with open (file_path_2, 'a') as data_f:
                data_f.write (f'{p[i]}')   

for i in range(len(b)):
    if i < int (len(b) - 1):
        uncompress(b[i])
        with open (file_path_2, 'a') as data_f:
            data_f.write (' ')
    if i == int (len(b) - 1):
        uncompress(b[i])

with open (file_path_2, 'r') as data_f:
    print(f"Что в разсжатом файле: {data_f.readline()}")

os.remove(file_path_2)