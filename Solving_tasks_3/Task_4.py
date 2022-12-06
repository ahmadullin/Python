# Программа, которая будет преобразовывать десятичное число в двоичное.
n = int (input ("Введите значение: "))
num = n

a = []
while num != 0:
    k = num - ((int (num/2)) * 2)
    a.append(k)
    num = int (num/2)

b = []
for i in range (len(a)):
    k = a[(len(a) - 1) - i]
    b.append(k)

result = int(''.join(map(str, b)))

print (f"{n} --> {result}")