# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from os import remove
# функция заполнения списка чисел
def List_number ():
    new_list_number = input('Введите список чисел через пробел ')
    new_list_number = new_list_number.split()
    return new_list_number

# функция нахождения неповтора
def NoRepeat (newList):
    no_repeat_list = []
    for i in newList:
        if newList.count(i) > 1:
           continue
        else:
            no_repeat_list.append(i)       
    return no_repeat_list


newList1 = List_number()
print(NoRepeat(newList1))


