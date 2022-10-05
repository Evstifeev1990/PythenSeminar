# Задать список из n чисел последовательности (1+ 1 ) и вывести на экран их сумму.n

import math
new = int(input('Введите число n '))
if new != 0:
    i = 1
    while i < new:
        work = math.pow((1+1/i), i)
        i += 1
        print(work, end=', ')
    print(math.pow((1+1/new), new))
else:
    print('Введите корректное число! )))) не 0')