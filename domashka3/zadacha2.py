# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# функция заполнения списка чисел
def List_number ():
    new_list_number = input('Введите список чисел через пробел ')
    new_list_number = new_list_number.split()
    return new_list_number

def Pair_nambers (list_num):
    list_len = len(list_num)
    pair_list = []
    for i in range(0, round(list_len/2)):
        pair_list.append(int(list_num[i])*int(list_num[list_len-(i+1)]))
    
    print(pair_list)


Pair_nambers(List_number())

