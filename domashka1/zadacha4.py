# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти '))

def Diapazon(number):
    if number == 1:
        print('x>0 and y>0')
    elif number == 2:
        print('x>0 and y<0')
    elif number == 3:
        print('x<0 and y<0')
    elif number == 4:
        print('x<0 and y>0')

Diapazon(quarter)