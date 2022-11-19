
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0


from sympy import *
import matplotlib.pyplot as plt

print('Определить корни')
x = Symbol('x')
func = 5*x**2+10*x-30
y = solve(func)
x1 = round(float(y[0]), 2)
x2 = round(float(y[1]), 2)
print(x1, x2)

print('Интервалы, на которых функция возрастает')
fd = diff(func)
print(solve(0 < fd))

print('Интервалы, на которых функция убывает')
print(solve(fd < 0))

print('Построить график')
list_y = []
for i in range(-5, 6):
    x = i
    y = 5*x**2+10*x-30
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6), list_y)
plt.grid()
plt.show()

print('Вычислить вершину')
corni = solve(fd)
top = corni[0]
x = top
y = 5*x**2+10*x-30
print(top, y)

print('Определить промежутки, на котором f > 0')
print(solve(0 < func))

print('Определить промежутки, на котором f < 0')
print(solve(func < 0))
