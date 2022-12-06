# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

num = int (input ("Сколько чисел будет в списке: "))

a = []
for i in range (num):
    k = float (input (f"Введите {i+1}-ое значение: "))
    a.append(k)

max = round((a[1]*10)%10,2)
min = round((a[1]*10)%10,2)

for i in range (num):
    if round((a[i]*10)%10,2) > max: max = round((a[i]*10)%10,2)
    if round((a[i]*10)%10,2) < min: min = round((a[i]*10)%10,2)

print (f"{a} --> {max} - {min} = {max-min}")