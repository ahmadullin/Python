# Алгоритм перемешивания списка
import random

num = int (input ("Из скольки элементов будет список? Введите значение: "))

a = []
for _ in range (num):
    k = input ("Введите элемент: ")
    a.append(k)

print (f"Список: {a}")

opros = input ("Перемешать порядок элементов: ")

if ("а" in opros) == True:
    random.shuffle(a)
    print(a)
else:
    print("Ok")