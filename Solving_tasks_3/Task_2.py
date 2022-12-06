# Программа, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

num = int (input ("Сколько чисел будет в списке: "))

a = []
for i in range (num):
    k = int (input (f"Введите {i+1}-ое значение: "))
    a.append(k)

b = []
if num%2 == 0:
    for i in range (int(num/2)):
        z = a[i] * a[int(num - 1) - i]
        b.append(z)
else:
    for i in range (int((num/2)+1)):
        z = a[i] * a[int(num - 1) - i]
        b.append(z)

print (f"{a} --> {b}")