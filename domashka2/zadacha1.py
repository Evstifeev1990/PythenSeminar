# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

namber = input('Введите вещественное число ')
summa = 0
i = 0
while i < len(namber):
    if namber[i]== ",": # почему не работает or ?
        i+=1
    elif namber[i]== ".":
        i+=1
    else: 
        namb=int(namber[i])
        summa+=namb
        i+=1
print(f'Сумма цифр = {summa}')
      
