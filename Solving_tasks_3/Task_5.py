# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int (input ("Введите значение: "))

a = []
b = []
for i in range (num + 1):
    if i == 0: k = 0
    if i == 1: k = 1
    if i > 1:
        k = a[i-1] + a[i-2]
    a.append(k)
    b.append(k)

for i in range (2, num + 1, 2):
    b[i] = b[i]*(-1)


print (b[::-1] + a)