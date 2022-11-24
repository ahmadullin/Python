# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

a = []
for i in range (3):
    a.append(int (input (f'Введите {i+1}-ое значение: ')))

print (a)

b = not (a[1] or a[2] or a[3])
c = not a[1] and not a[2] and not a[3]

if b == c: print (True)
else: print (False)