# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random
print ("Жеребьевка: определяется первый ход с помощью игрального кубика")

kub_player_1 = random.randint(1, 6)
print (f"Значение игрального кубика Игрок_1: {kub_player_1}")
kub_player_2 = random.randint(1, 6)
print (f"Значение игрального кубика Игрок_2: {kub_player_2}")

if kub_player_1 > kub_player_2:
    player_1 = 'Игрок_1'
    player_2 = 'Игрок_2'
    i = 0
else:
    player_1 = 'Игрок_2'
    player_2 = 'Игрок_1'
    i = 1


print (f"Начинает {player_1}")

def play(num, i):

    print (f"\nОсталось {num} конфет")
    
    if i == 0: player = player_1
    if i == 1: player = player_2
    print (f"Ход {player}")

    x = int (input ("Можно взять от 1 до 28 конфет. Сколько конфет возьмешь? --> "))
    while (x > 29) or (x < 1):
        x = int (input ("Введи значение от 1 до 28 --> "))
    while x > num:
        x = int (input (f"Осталось не так много конфет. Введи значение от 1 до {num} --> "))
    result = num - x
    if result > 0 and i == 0: return play(num - x, i+1)
    if result > 0 and i == 1: return play(num - x, i-1)
    else: print (f"Победил {player}")

        
num = int (input ("Сколько будет конфет в игре: "))

play (num, i)