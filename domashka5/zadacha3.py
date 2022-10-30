# Создайте программу для игры в "Крестики-нолики".


new_list_krest = []
# выведем поле


def Pole():
    print('Дано поле для игры')
    for i in range(0, 4, 1):
        print(f'{i} ', end='')
    print()
    for i in range(1, 4, 1):
        print(i, end='')
        for j in range(1, 4, 1):
            print(f' -', end='')
        print()

# запустим игру


def Krest(krest_slov):
    # вводит координату игрок икс
    while len(krest_slov)>0:
        krest_х = int(input('Игрок - Крестик - Введите координату сначало y (вертикаль), потом х (горизонталь) без пробела '))
        if 11 <= krest_х <= 13 or 21 <= krest_х <= 23 or 31 <= krest_х <= 33:
            if krest_slov[krest_х] == '-':
                krest_slov[krest_х] = 'X'
                for i in range(11, 14, 1):
                    print(krest_slov[i], end=''+' ')
                print()
                for i in range(21, 24, 1):
                    print(krest_slov[i], end=''+' ')
                print()
                for i in range(31, 34, 1):
                    print(krest_slov[i], end=''+' ')
                print()
            else:
                print('Координата занята')
                continue
        else:
            print('Введена неверная координата')
            continue  
        break
    # функция проверки победы   
    def Proverka(krest_slov, iks):
        if krest_slov[11] == iks and krest_slov[12] == iks and krest_slov[13] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[21] == iks and krest_slov[22] == iks and krest_slov[23] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[31] == iks and krest_slov[32] == iks and krest_slov[33] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[11] == iks and krest_slov[21] == iks and krest_slov[31] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[12] == iks and krest_slov[22] == iks and krest_slov[32] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[13] == iks and krest_slov[23] == iks and krest_slov[33] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[11] == iks and krest_slov[22] == iks and krest_slov[33] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        elif krest_slov[31] == iks and krest_slov[22] == iks and krest_slov[13] == iks:
            print(f'Победа {iks} УРАААА!!!!')
        else:
            return 'game'
    # проверка победы крест
    if Proverka(krest_slov, 'X') == 'game':
        # вводит координату игрок ноль
        while len(krest_slov)>0:
            krest_o = int(input('Игрок - нолик - Введите координату сначало y (вертикаль), потом х (горизонталь) без пробела '))
            if 11<=krest_o<=13 or 21<=krest_o<=23 or 31<=krest_o<=33:
                if krest_slov[krest_o] == '-':
                    krest_slov[krest_o] = 'O'
                    for i in range(11, 14, 1):
                        print(krest_slov[i], end=''+' ')
                    print()
                    for i in range(21, 24, 1):
                        print(krest_slov[i], end=''+' ')
                    print()
                    for i in range(31, 34, 1):
                        print(krest_slov[i], end=''+' ')
                    print()
                else:
                    print('Координата занята')
                    continue
            else:
                print('Введена неверная координата')
                continue
            break
        # проверка победы ноль
        if Proverka(krest_slov, 'O') == 'game':
            Krest(krest_slov)
    else: 
        print('Игра окончена')

Pole()
krest_null = {11: '-', 12: '-', 13: '-', 21: '-', 22: '-', 23: '-', 31: '-', 32: '-', 33: '-'}
Krest(krest_null)
