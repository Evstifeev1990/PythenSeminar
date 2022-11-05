import sqlite3
import view

bd = sqlite3.connect("Data_base.db")

cursor = bd.cursor()
    
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        name TEXT,
        last_name TEXT,
        institute_group TEXT,
        course INTEGER,
        scholarship INTEGER
    )''')    
bd.commit()
n=1
while n>0:
    punkt = view.menu()
    if punkt == 1:
        try:
            cursor.executemany('INSERT INTO student VALUES(?,?,?,?,?,?)', view.vvod_dannykh())
            bd.commit()
        except:
            print()
            print('Данные не записаны. Такой id уже существует')
    elif punkt == 2:
        print()
        for i in cursor.execute('SELECT * FROM student'):
            print(*i)
    elif punkt == 3:
        new_punkt = input('Введите SQLite запрос - \n')
        cursor.execute(new_punkt)
        one = cursor.fetchone()
        print(one)
    elif punkt == 4:
        id_del = int(input('Введите значение id для удаления - '))
        cursor.execute(f'DELETE FROM student WHERE id={id_del}')
        bd.commit()
    else:
        break