# Подумайте как наделить бота "интеллектом"

import random

def Hod_igrok(number_can, name_p):
    while number_can != 0:
        print(f'На столе {number_can} конфет')
        hod = int(input(f'{name_p[0]} - делайте ход (не забываем от 1 до 28) - '))
        if 1 <= hod <= 28 and hod <= number_can:
            number_can -= hod
            break
        else:
            print('ход неверен')
            continue
    return number_can

def Hod_bot(number_candi, name_pl):
    while number_candi != 0:
        print(f'На столе {number_candi} конфет')
        if number_candi<=28:
            hod = number_candi
            number_candi-=hod
            if number_candi == 0:
                print(f'игрок бот победил!!!!!!')
                break
        if number_candi%29 == 0:
            hod = random.randint(1, 28)
            number_candi-=hod
            print(f'бот сделал ход, равный = {hod}')
            break
        else:
            hod = number_candi%29
            number_candi-=hod
            print(f'бот сделал ход, равный = {hod}')
            while number_candi != 0:
                print(f'На столе {number_candi} конфет')
                hod = int(input(f'{name_pl[0]} - делайте ход (не забываем от 1 до 28) - '))
                if 1 <= hod <= 28 and hod <= number_candi:
                    number_candi -= hod
                else:
                    print('ход неверен')
                    continue
                if number_candi == 0:
                    print(f'игрок {name_pl[0]} победил!!!!!!')
                    break
                print(f'На столе {number_candi} конфет')
                hod = 29 - hod
                number_candi-=hod
                print(f'бот сделал ход, равный = {hod}')
                if number_candi == 0:
                    print(f'игрок бот победил!!!!!!')
                    break
            break
    return number_candi


number_candies = int(input('Введите количество конфет большее 56 = '))
print(f'Начинаем игру. На столе {number_candies} конфета. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')

name_play = []
name_play.append(input('Введите своё имя '))
name_play.append('бот')

i = random.randint(0, 1)
print(f'Право первого хода предоставляется - {name_play[i]}')
if i == 1:
    name_play[0], name_play[1] = name_play[1], name_play[0]

print(name_play)



if name_play[0] == 'бот':
    print(f'На столе {number_candies} конфет')
    hod = number_candies%29
    number_candies-=hod
    print(f'бот сделал ход, равный = {hod}')
    while number_candies != 0:
        print(f'На столе {number_candies} конфет')
        hod = int(input(f'{name_play[-1]} - делайте ход (не забываем от 1 до 28) - '))
        if 1 <= hod <= 28 and hod <= number_candies:
            number_candies -= hod
        else:
            print('ход неверен')
            continue
        if number_candies == 0:
            print(f'игрок {name_play[-1]} победил!!!!!!')
            break
        while number_candies != 0:
            print(f'На столе {number_candies} конфет')
            if number_candies > 28:
                hod = 29 - hod
                print(f'бот сделал ход, равный = {hod}')
                number_candies -= hod
                break
            else:
                hod = number_candies
                number_candies -= hod
        if number_candies == 0:
            print(f'игрок бот победил!!!!!!')
            break    
else:
    while number_candies != 0:
        number_candies = Hod_igrok(number_candies, name_play)
        if number_candies == 0:
            print(f'игрок {name_play[0]} победил!!!!!!')
            break
        number_candies = Hod_bot(number_candies, name_play)
        if number_candies == 0:
            break




        


