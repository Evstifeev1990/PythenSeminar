# Написать программу получающую набор произведений чисел от 1 до N.

new = int(input('Введите число n '))
work=1
while new >1:
    work*=new
    new-=1
print(f'n факториал = {work}')