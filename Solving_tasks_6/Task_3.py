# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#num = int (input ("Какая будет длина списка? --> "))
#a = []
#for i in range (num):
#    k = int (input (f"Введите {i+1}-ое значение: "))
#    a.append(k)

#b = []
#for i in range (len(a)):
#    if (a.count(a[i])) < 2:
#        b.append(a[i])

#print (f"Введенный список: {a}")    
#print (f"Числа, которые не повторяются: {b}")  


num = int (input ("Какая будет длина списка? --> "))

a = [int (input (f"Введите {i+1}-ое значение: ")) for i in range (num)]

b = [a[i] for i in range (len(a)) if (a.count(a[i])) < 2]


print (f"Введенный список: {a}")    
print (f"Числа, которые не повторяются: {b}")  

# Было 11 строчек кода, стало 5