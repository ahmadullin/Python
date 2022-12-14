# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

# num_run = int (input("Введите любое положительное число (N>0): "))
# while num_run <= 0:
#     num_run = int (input("Введите любое положительное число (N>0): "))

# a = []
# for i in range (-num_run, num_run + 1):
#     a.append(i)
# print(a)

# num_index = input("Введите индексы чисел, произведение которых надо найти: ")

# b = []
# for i in range (num_index.count(' ') + 1):
#     k = int (num_index.split(' ')[i])
#     if (-1) < k <= (num_run * 2):
#         b.append(k)

# print (f"Индексы, котрые есть в списке чисел: {b}")
 
#opros = input("Найти произведение по этим числам или начать снова? (Да/Нет): ")

# result = 1
# if ("а" in opros) == True:
#     for i in range (len(b)):
#         result = result * a[b[i]]
#         print (f"Произведение чисел под указанными индексами равно: {result}")
# else:
#     print("Ok")

while (num := int (input("Введите любое положительное число (N>0): "))) <= 0:
    print("Попробуйте еще раз")

a = [i for i in range (-num, num + 1)]

print(a)

num_index = input("Введите индексы чисел, произведение которых надо найти: ")

b = [int (i) for i in num_index.split(' ') if (-1) < int (i) <= (num * 2)]

print (f"Индексы, котрые есть в списке чисел: {b}")

opros = input("Найти произведение по этим числам или начать снова? (Да/Нет): ")

result = 1
if ("а" in opros) == True:
        for i in range (len(b)):
            result = result * a[b[i]]
        print (f"Произведение чисел под указанными индексами равно: {result}")
else:
    print("Ok")

# было 22 строчек кода, стало 15 