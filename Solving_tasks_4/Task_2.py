# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

while (num := int (input ("Введите натуральное число: "))) < 1:
    print ("Попробуйте снова...")

a = set ()

def f(x,i):
    while x != 1:
        if x % i == 0:
            a.add (i)
            return f(x/i, i)
        else: 
            return f(x, i+1)
f(num, 2)
print (f"Простые множители числа {num}: {a}")