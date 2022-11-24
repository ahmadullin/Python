# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

number_x1 = int (input ('Введите значение X1: '))
number_y1 = int (input ('Введите значение Y1: '))
number_x2 = int (input ('Введите значение X1: '))
number_y2 = int (input ('Введите значение Y1: '))

result = math.sqrt((number_x2 - number_x1)**2 + (number_y2 - number_y1)**2)

print (round (result,3))