# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file1.txt', 'w') as f:
    f.write('ffffhhhhhsssnnnfffjjjssgggcckkkssshhhccgfgnhjh')

fale1 = open('file1.txt')
fale1 = fale1.read()+'-'
amount = 0
name = ''
fale2 = ''
amount = 1
for index in range(0, len(fale1)-1, 1):
    name = fale1[index]
    if fale1[index] == fale1[index+1]:
        amount+=1
    else:
        fale2 = fale2 + str(amount) + fale1[index]
        amount = 1

print(fale2)

with open('file2.txt', 'w') as n:
    n.write(fale2)