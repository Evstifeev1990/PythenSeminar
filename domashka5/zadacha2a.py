# Создайте программу для игры с конфетами человек против бота.

import random

print('Начинаем игру. На столе 120 конфет. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')

name_play = []
name_play.append(input('Введите своё имя '))
name_play.append('бот')

i = random.randint(0, 1)
print(f'Право первого хода предоставляется - {name_play[i]}')
if i == 1:
    name_play[0], name_play[1] = name_play[1], name_play[0]

print(name_play)
number_candies = 120
if name_play[0] == 'бот':
    while number_candies != 0:
        print(f'На столе {number_candies} конфет')
        if number_candies >= 28:
            hod = random.randint(1, 28)
            print(f'бот сделал ход, равный = {hod}')
            number_candies -= hod
        else:
            hod = random.randint(0, number_candies)
            print(f'бот сделал ход, равный = {hod}')
            number_candies -= hod
        if number_candies == 0:
            print(f'игрок бот победил !!!!!!!3')
            break
        while number_candies != 0:
            print(f'На столе {number_candies} конфет')
            hod = int(input(f'{name_play[-1]} - делайте ход (не забываем от 1 до 28) - '))
            if 1 <= hod <= 28 and hod <= number_candies:
                number_candies -= hod
                break
            else:
                print('ход неверен')
                continue
        if number_candies == 0:
            print(f'игрок {name_play[-1]} победил!!!!!!')
            break

while number_candies != 0:
    print(f'На столе {number_candies} конфет')
    hod = int(input(f'{name_play[0]} - делайте ход (не забываем от 1 до 28) - '))
    if 1 <= hod <= 28 and hod <= number_candies:
        number_candies -= hod
    else:
        print('ход неверен')
        continue
    if number_candies == 0:
        print(f'игрок {name_play[0]} победил!!!!!')
        break
    while number_candies != 0:
        print(f'На столе {number_candies} конфет')
        if number_candies >= 28:
            hod = random.randint(1, 28)
            print(f'бот сделал ход, равный = {hod}')
            number_candies -= hod
        else:
            hod = random.randint(0, number_candies)
            print(f'бот сделал ход, равный = {hod}')
            number_candies -= hod
        if number_candies == 0:
            print(f'игрок бот победил !!!!!!')
            break
        else:
            break

        
    
    
