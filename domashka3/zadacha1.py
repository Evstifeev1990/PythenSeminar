# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# функция заполнения списка чисел
def List_number ():
    new_list_number = input('Введите список чисел через пробел ')
    new_list_number = new_list_number.split()
    return new_list_number

# функция суммы чисел нечётных позиций
def Sum_odd_position(list_num):
    list_len = len(list_num)
    sum = 0
    for i in range(1, list_len, 2):
        sum+=int(list_num[i])
    return sum

print(f'сумма чисел нечётных позиций = {Sum_odd_position(List_number())}')