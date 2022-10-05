# Реализовать алгоритм перемешивания списка.

import random

new = int(input('Введите число n '))
newlist = list(range(new*-1, new+1))
print(newlist)
twolist = []
i = 0
while i < len(newlist):
    n=random.randint(0,len(newlist)-1)
    if newlist[n] not in twolist:
        twolist.append(newlist[n])
        i+=1
print(twolist)
