# Программа, которая принимает на вход вещественное число и показывает сумму его цифр.

num =  input ("Введите вещественное число: ")

while (('.' in (num)) == False): # Проверка наличия "."
    num =  input ("Введите вещественное число: ")

while ((num.split ('.')[0]).isdigit()) == False: # Проверка все ли числа до "." - цифры
    num =  input ("Введите вещественное число: ")

while ((num.split ('.')[1]).isdigit()) == False: # Проверка все ли числа после "." - цифры
    num =  input ("Введите вещественное число: ")

num_1 =  (num.split ('.')[0])
num_2 =  (num.split ('.')[1])

def f(x):
    sum = 0
    for i in range (len(x)):
        sum = sum + (int (x[i]))
    return sum

result = f(num_1) + f(num_2)

print (f"Сумма цифр числа равна: {result}")