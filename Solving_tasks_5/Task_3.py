# Программа для игры в ""Крестики-нолики""

import random
print ("\nЖеребьевка: определяется первый ход с помощью игрального кубика\n")

kub_player_1 = random.randint(1, 6)
print (f"Значение игрального кубика Игрок_1: {kub_player_1}")
kub_player_2 = random.randint(1, 6)
print (f"Значение игрального кубика Игрок_2: {kub_player_2}")

if kub_player_1 > kub_player_2:
    player_1 = 'Игрок_1'
    player_2 = 'Игрок_2'
    i = 0
    print (f"Начинает {player_1}")
else:
    player_1 = 'Игрок_1'
    player_2 = 'Игрок_2'
    i = 1
    print (f"Начинает {player_2}")

def play(s,i):
    print('\n')

    print(f'_{s[0]}_|_{s[1]}_|_{s[2]}_')
    print(f'_{s[3]}_|_{s[4]}_|_{s[5]}_')
    print(f' {s[6]} | {s[7]} | {s[8]} ')
    
    if i == 0:
        player = player_1
        print (f"Ход {player}. Ставит 'X'")

        x = int (input ("Какую ячейку закрыть? --> "))
        while (x > 9) or (x < 1):
            x = int (input ("Введи значение от 1 до 9 --> "))
        while (s[x-1] == 'X') or (s[x-1] == 'O'):
            x = int (input ("Ячейка занята. Введите другое значение --> "))
        s[x-1] = 'X'

        if (s[0] == s[1] == s[2]) or (s[3] == s[4] == s[5]) or (s[6] == s[7] == s[8]) \
            or (s[0] == s[3] == s[6]) or (s[1] == s[4] == s[7]) or (s[2] == s[5] == s[8]) \
                or (s[0] == s[4] == s[8]) or (s[6] == s[4] == s[2]): print(f"Победа {player}")
        else:
            if i == 0: return play(s, i+1)

    if i == 1:
        player = player_2
        print (f"Ход {player}. Ставит 'O'")

        o = int (input ("Какую ячейку закрыть? --> "))
        while (o > 9) or (o < 1):
            o = int (input ("Введи значение от 1 до 9 --> "))
        while (s[o-1] == 'X') or (s[o-1] == 'O'):
            o = int (input ("Ячейка занята. Введите другое значение --> "))
        s[o-1] = 'O'
        
        if (s[0] == s[1] == s[2]) or (s[3] == s[4] == s[5]) or (s[6] == s[7] == s[8]) \
            or (s[0] == s[3] == s[6]) or (s[1] == s[4] == s[7]) or (s[2] == s[5] == s[8]) \
                or (s[0] == s[4] == s[8]) or (s[6] == s[4] == s[2]): print(f"Победа {player}")
        else:
            if i == 1: return play(s, i-1)
    

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

play (s,i)