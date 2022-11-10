from tictactoe import Board
import random


def proverka(viva, nama):
        if '00' in viva and '10' in viva and '20' in viva:
            print(f'Урааа!!! {nama} вин!!!')           
        elif '01' in viva and '11' in viva and '21' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '02' in viva and '12' in viva and '22' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '00' in viva and '01' in viva and '02' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '10' in viva and '11' in viva and '12' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '20' in viva and '21' in viva and '22' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '00' in viva and '11' in viva and '22' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        elif '20' in viva and '11' in viva and '02' in viva:
            print(f'Урааа!!! {nama} вин!!!')
        else:
            return 1
print('Крестики - нолики, приступим!!!')
name1 = input('Введите имя первого игрока - ')
name2 = input('Введите имя второго игрока - ')
print('Начинается случайный выбор игрока первого хода (крестик)')
gamer = [name1, name2]
ruleytka = random.randint(0, 1)
if ruleytka == 0:
    print(f'Первый игрок (крестик) это - {name1}')
    print(f'Второй игрок (нолик) это - {name2}')
else:
    name1, name2 = name2, name1
    print(f'Первый игрок (крестик) это - {name1}')
    print(f'Второй игрок (нолик) это - {name2}')

print('Рисуем доску 3х3')
board = Board(dimensions=(3, 3))
print(board)
vivat1 = []
vivat2 = []
a = 1
while a > 0:
    hod1 = input(f'Игрок {name1} введите координату крестика через запятую - ')
    hod1 = hod1.split(',')
    board.push((int(hod1[0]), int(hod1[1])))
    print(board)
    hod1 = hod1[0] + hod1[1]
    vivat1.append(hod1)
    prov = proverka(vivat1, name1)
    if prov != 1:
        break
    hod2 = input(f'Игрок {name2} введите координату нолика через запятую - ')
    hod2 = hod2.split(',')
    board.push((int(hod2[0]), int(hod2[1])))
    print(board)
    hod2 = hod2[0] + hod2[1]
    vivat2.append(hod2)
    prov1 = proverka(vivat2, name2)
    if prov1 != 1:
        break