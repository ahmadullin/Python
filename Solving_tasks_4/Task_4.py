# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random, os

while (num := int (input ("Введите натуральное число: "))) < (0):
    print ("Попробуйте снова...")

file_path = r"C:\Users\1\Desktop\Python\Solving_tasks_4\Task_4.txt"
def f(x):
    while x >= 0:
        a = random.randint(0, 100)
        
        if x > 1:
            if a > 1:
                with open (file_path, 'a') as f_data:
                    f_data.write (f'{a}*x^{x}')
            if a == 1:
                with open (file_path, 'a') as f_data:
                    f_data.write (f'x^{x}')
            if a == 0:
                with open (file_path, 'a') as f_data:
                    f_data.write ('')    
        
        if x == 1: 
            if a > 1:
                with open (file_path, 'a') as f_data:
                    f_data.write (f'{a}*x')
            if a == 0:
                with open (file_path, 'a') as f_data:
                    f_data.write ('')
        
        if x == 0:
            if a > 0:
                with open (file_path, 'a') as f_data:
                    f_data.write (f'{a}')
    
            if a == 0:
                with open (file_path, 'a') as f_data:
                    f_data.write ('')
        
        if x != 0:
            with open (file_path, 'a') as f_data:
                    f_data.write (' + ')
        else:
            with open (file_path, 'a') as f_data:
                    f_data.write (' = 0')
        
        return f(x-1)

f(num)

with open (file_path, 'r') as f_data:
    print (f_data.readline ())

os.remove(file_path)