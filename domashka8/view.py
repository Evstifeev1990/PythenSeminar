
def vvod_dannykh():
    id = int(input('Введите порядковый номер (id) студента - '))
    name = input('Введите имя студента - ')
    last_name = input('Введите фамилию студента - ')
    institute_group = input('Введите название группы студента - ')
    course = int(input('Введите курс студента - '))
    scholarship = int(input('Введите сумму стипендии студента (руб.) - '))
    baza = [(id, name, last_name, institute_group, course, scholarship)]
    return baza


def menu():
    print()
    punkt_menu = int(input('Выберити пункт меню:\n 1 - добавление записи\n 2 - просмотр\n 3 - поиск\n 4 - удаление\n 5 - выход \n'))
    return punkt_menu