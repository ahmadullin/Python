# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

number_x = int (input (f'Введите значение X (не равен 0): '))
while number_x == 0:
    number_x = int (input (f'Введите значение X (не равен 0): '))

number_y = int (input (f'Введите значение Y (не равен 0): '))
while number_y == 0:
    number_y = int (input (f'Введите значение Y (не равен 0): '))

if number_x > 0 and number_y > 0: print ("1")
if number_x < 0 and number_y > 0: print ("2")
if number_x < 0 and number_y < 0: print ("3")
if number_x > 0 and number_y < 0: print ("4")