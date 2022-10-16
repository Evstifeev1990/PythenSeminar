# 1 Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10

import math
newList = []
for i in range(-1, -10, -1):
    newList.append(str(10**i))
print(newList)

newD = input('Введите любое число из данного списка: ')
newD = newD.replace(',','.')
if newD in newList:
    print('Введите числа a и b с условием a/b получается иррациональное число')
    newNumber1 = float(input('a = '))
    newNumber2 = float(input('b = '))
    print(round((newNumber1/newNumber2), len(newD)-2))
else:
    print('Введено неверное число')



