# Удаление абв

# функция заполнения списка чисел
def List_number ():
    new_list = input('Введите список слов через пробел ')
    new_list= new_list.split()
    return new_list


print(list(filter(lambda x: 'абв' not in x, List_number())))