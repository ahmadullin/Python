# 0.6x^3+5.5x^2+10x -5 = 0
import matplotlib.pyplot as plt

print ('\nПодходит для решения уравнений типа:\nax^3 + bx^2 + cx + d = 0,\nгде a,b,c,d !=0')

numbers = []
print ('\nВведите уравнение: \n')
a = float (input('Коэффициент a (a*x^3) = '))
numbers.append(a)
b = float (input('Коэффициент b (b*x^2) = '))
numbers.append(b)
c = float (input('Коэффициент c (c*x^1) = '))
numbers.append(c)
d = float (input('Коэффициент d (d*x^0) = '))
numbers.append(d)

if (int(a) != a) or (int(b) != b)  or (int(c) != c) or (int(d) != d):
    for i in range(4):
        numbers[i] = numbers[i] * 10


if a > 0:
    if b > 0:
        if c > 0:
            if d > 0: print(f'\n{a}*x^3 + {b}*x^2 + {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 + {b}*x^2 + {c}*x^1 {d}*x^0 = 0\n')
        else:
            if d > 0: print(f'\n{a}*x^3 + {b}*x^2 {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 + {b}*x^2 {c}*x^1 {d}*x^0 = 0\n')
    else:
        if c > 0:
            if d > 0: print(f'\n{a}*x^3 {b}*x^2 + {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 {b}*x^2 + {c}*x^1 {d}*x^0 = 0\n')
        else:
            if d > 0: print(f'\n{a}*x^3 {b}*x^2 {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 {b}*x^2 {c}*x^1 {d}*x^0 = 0\n')
else:
    if b > 0:
        if c > 0:
            if d > 0: print(f'\n{a}*x^3 + {b}*x^2 + {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 + {b}*x^2 + {c}*x^1 {d}*x^0 = 0\n')
        else:
            if d > 0: print(f'\n{a}*x^3 + {b}*x^2 {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 + {b}*x^2 {c}*x^1 {d}*x^0 = 0\n')
    else:
        if c > 0:
            if d > 0: print(f'\n{a}*x^3 {b}*x^2 + {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 {b}*x^2 + {c}*x^1 {d}*x^0 = 0\n')
        else:
            if d > 0: print(f'\n{a}*x^3 {b}*x^2 {c}*x^1 + {d}*x^0 = 0\n')
            else: print(f'\n{a}*x^3 {b}*x^2 {c}*x^1 {d}*x^0 = 0\n')


if int(a) == a: a = int(a)
if int(b) == b: b = int(b)
if int(c) == c: c = int(c)
if int(d) == d: d = int(d)


print(numbers)

def num(k):
    num = []
    i = 1
    if k < 0: k = k * (-1)
    while i != (k + 1):
        if k % i == 0:
            num.append(i)
            i = i + 1
        else: i = i + 1    
    return num

numbers_a = num(numbers[0])

numbers_d = num(numbers[3])

numbers_x = []
for i in numbers_a:
    for j in numbers_d:
        numbers_x.append(float(i/j))
        numbers_x.append(((-1) * (i/j)))

numbers_x = sorted (numbers_x)
print(numbers_x)

x = []
y_on = []
y_off = []
for i in numbers_x:
    y = int((numbers[0]*(i*i*i)) + (numbers[1]*(i*i)) + (numbers[2]*i) + (numbers[3])) 
    if y == 0: x.append(i)
    if y > 0: y_on.append(i)
    if y < 0: y_off.append(i)
    plt.plot (y, (a*(i*i*i)) + (b*(i*i)) + (c*i) + (d))
    plt.show()

print (f'\nКорни уравнения = {x}\n')
print (f'\nФункция возрастает при x = {y_on}\n')
print (f'\nФункция убывает при x = {y_off}\n')


plt.plot (x, (a*(x*x*x)) + (b*(x*x)) + (c*x) + (d))
plt.show()