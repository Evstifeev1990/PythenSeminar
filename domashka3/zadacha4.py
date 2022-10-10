# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

new = int(input('Введите число n '))

def Funk (number):
    new_number = ''
    while number!=0:
        new_number = str(number%2)+new_number
        number = number//2
    return int(new_number)

print(Funk(new))