# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


fib1 = fib2 = 1
minusfib1 = 1
minusfib2 = -1
n = int(input('Введите число '))
b = [-1, 1, 0, 1, 1]
if n == 0:
    print('[0]')
elif n == 1:
    print ("[1, 0, 1]")
elif n == 2:
    print (b)
else:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        b.append(fib2)
        a = minusfib2
        minusfib2 = minusfib1 - minusfib2
        minusfib1 = a
        b.insert(0, minusfib2)
    print(b)


