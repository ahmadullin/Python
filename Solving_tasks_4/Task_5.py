# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

import random, os

while (num_1 := int (input ("Введите 1-ое натуральное число: "))) < (0):
    print ("Попробуйте снова...")
while (num_2 := int (input ("Введите 2-ое натуральное число: "))) < (0):
    print ("Попробуйте снова...")    

file_path_1 = r"C:\Users\1\Desktop\Python\Solving_tasks_4\Task_5_1.txt"
file_path_2 = r"C:\Users\1\Desktop\Python\Solving_tasks_4\Task_5_2.txt"
file_result = r"C:\Users\1\Desktop\Python\Solving_tasks_4\Task_5_result.txt"

def touchNewFile(file_path, x):
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
            if a != 0:
                with open (file_path, 'a') as f_data:
                    f_data.write (' + ')
            if a == 0:
                with open (file_path, 'a') as f_data:
                    f_data.write ('')
        else:
            with open (file_path, 'a') as f_data:
                    f_data.write (' = 0')
        
        return touchNewFile(file_path, x-1)

touchNewFile(file_path_1, num_1)
touchNewFile(file_path_2, num_2)

def fileToStr(file_path):
    with open (file_path, 'r') as f_data:
        str = f_data.readline ()
        print (f'Заданное уравнение: {str}')
    os.remove(file_path)
    return str

a = fileToStr(file_path_1)
b = fileToStr(file_path_2)

def clearStr (str: str):
    str = str.replace(' = 0', '')
    str = str.replace(' ', '')
    str = str.split ('+')
    return str

a = clearStr (a)
b = clearStr (b)

print(a)
print(b)

z_a = []
k_b = []

def newList(p,l):
    for i in range(len(l)):
        if '^' in l[i]:
            l[i] = l[i].split('*x^')
            p.append(l[i])
        else:
            if 'x' in l[i]:
                l[i] = l[i].replace('*x', ' 1')
                l[i] = l[i].split(' ')
                p.append(l[i])
            else:
                l[i] = [l[i], '0']
                p.append(l[i])
    return(p)


print(newList(z_a,a))
print(newList(k_b,b))


def result(m,n):
    for i in m:
        for j in n:
            if i[1] == j[1]:

                if int (i[1]) > 1:
                    with open (file_result, 'a') as f_data:
                        f_data.write (f'{int(i[0]) + int(j[0])}*x^{i[1]} + ')
                
                if int (i[1]) == 1:
                    with open (file_result, 'a') as f_data:
                        f_data.write (f'{int(i[0]) + int(j[0])}*x + ')
                
                if int (i[1]) < 1:
                    with open (file_result, 'a') as f_data:
                        f_data.write (f'{int(i[0]) + int(j[0])} = 0')

result(z_a,k_b)
with open (file_result, 'r') as f_data:
        print (f'Решенное уравнение (складываются числа, у которых "х" в одинаковых степенях): {f_data.readline ()}')
os.remove(file_result)