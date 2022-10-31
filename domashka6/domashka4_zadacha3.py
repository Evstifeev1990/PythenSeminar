# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from os import remove
# функция заполнения списка чисел
def List_number ():
    new_list_number = input('Введите список чисел через пробел ')
    new_list_number = new_list_number.split()
    return new_list_number

newList1 = List_number()
print(list(filter(lambda x: newList1.count(x) == 1, newList1)))
