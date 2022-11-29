# Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int (input("Введите любое положительное число (N>0): "))
while num <= 0:
    num = int (input("Введите любое положительное число (N>0): "))

def f(x):
    result = 1
    for i in range (1,x+1):
        result = result * i
    return result

a = []
for i in range(num):
    k = f(i+1)
    a.append(k)

print (a)