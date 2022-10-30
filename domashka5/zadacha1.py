# функция заполнения списка чисел
def List_number ():
    new_list = input('Введите список слов через пробел ')
    new_list= new_list.split()
    return new_list

# функция удаления слов
def Del_word (new_list_word):
    for i in new_list_word:
        if 'абв' in i:
            new_list_word.remove(i)
    return new_list_word


list_word = List_number()
print(Del_word(list_word))