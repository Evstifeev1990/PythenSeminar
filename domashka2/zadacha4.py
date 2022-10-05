# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

new = int(input('Введите число n '))
newlist = list(range(new*-1, new+1))
print(newlist)
posishion = []
newnumber = []
mult = 1
long = int(input('Введите число позиций '))
while long > 0:
    number = int(input('Введите номер призиции меньше или равно 2*n '))
    if number<=new*2:
        posishion.append(number)
        newnumber.append(newlist[number])
        mult*=int(newlist[number])
        long -= 1
    else: print('Введите корректное число')
print(posishion)
print(newnumber)
print(f'Произведение чисел = {mult}')

