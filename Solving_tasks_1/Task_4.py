# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int (input ('Введите значение номер четверти координат: '))
while number > 4 or number < 1:
    number = int (input ('Введите значение номер четверти координат: '))

if number == 1: print ("X и Y от 0 до положительной бесконечности")
if number == 2: print ("X от 0 до отрицательной бесконечности, Y от 0 до положительной бесконечности")
if number == 3: print ("X и Y от 0 до отрицательной бесконечности")
if number == 4: print ("X от 0 до положительной бесконечности, Y от 0 до отрицательной бесконечности")