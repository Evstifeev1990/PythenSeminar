# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.


def List_number ():
    new_list_number = input('Введите список вещественных чисел через пробел ')
    new_list_number = new_list_number.replace(',','.')
    new_list_number = new_list_number.split()
    print(new_list_number)
    return new_list_number


def Fraction_difference (spisok):
    spisok_len = len(spisok)
    max = 0
    min = 1
    
    for i in range(0, spisok_len):
        spisok[i] = float(spisok[i])
        spisok[i] = spisok[i]%1
        if spisok[i] > max:
            max = spisok[i]
        if spisok[i] < min:
            min = spisok[i]
    return max - min
        


print(Fraction_difference(List_number()))