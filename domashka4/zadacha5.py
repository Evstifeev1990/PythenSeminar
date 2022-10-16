with open('file1.txt', 'w') as f:
    f.write('5x^2 + 6x^1 + 3 = 0')


with open('file2.txt', 'w') as n:
    n.write('7x^3 + 2x^2 + 4x^1 = 0')


f = open('file1.txt')
n = open('file2.txt')

f = f.read().split()
n = n.read().split()
print(f, n)
slovar = {}
slovar1 = {}

for i in f:
    if ('x' not in i) and (i != '+') and (i!='0') and (i != '='):
        newf = int(i)
    elif 'x' in i:
        slovar[i.split('x')[-1]] = i.split('x')[0]
    for j in n:    
        if ('x' not in j) and (j != '+') and (j != '0') and (j != '='):
            newf += int(j)    
        elif 'x' in j:
            slovar1[j.split('x')[-1]] = j.split('x')[0]
text = ''
if len(slovar.keys()) > len(slovar1.keys()):
    for q in slovar.keys():
        if q in slovar1.keys():
            slovar[q] = str(int(slovar[q])+int(slovar1[q]))
        text += slovar[q] + 'x' + q + ' + '
    text += str(newf) + ' = 0'
    print(text)
else:
    for q in slovar1.keys():
        if q in slovar.keys():
            slovar1[q] = str(int(slovar[q])+int(slovar1[q]))
        text += slovar1[q] + 'x' + q + ' + '
    text += str(newf) + ' = 0'
    print(text)


with open('file3.txt', 'w') as n:
    n.write(text)