# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


newList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

newNumber = int(input('Введите натуральное число: '))
mnog = []
if newNumber > 0:
     for i in newList:
        while newNumber%i == 0:
            mnog.append(i)
            newNumber = newNumber/i
else:
    print('Введено не натуральное число')

print(mnog)