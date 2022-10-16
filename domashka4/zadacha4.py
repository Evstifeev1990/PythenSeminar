# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

from random import randint

newNumber = int(input('Введите натуральное число от 0 до 100: '))
newList = ''
if 0<newNumber<100:
    for i in range(newNumber, 0, -1):
        newList+=(str(randint(0, 100))+'x'+'^'+str(i)+'+')
    newList+=(str(randint(0, 100)))+'=0'
else:
    print('Введено неверное число')

print(newList)


