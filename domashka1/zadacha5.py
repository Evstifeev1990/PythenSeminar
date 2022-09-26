# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

from cmath import sqrt
import math

namberAx = int(input('Введите координату Х точки А '))
namberAy = int(input('Введите координату Y точки А '))
namberBx = int(input('Введите координату X точки B '))
namberBy = int(input('Введите координату Y точки B '))


long = math.sqrt((math.pow((namberBx-namberAx),2))+(math.pow((namberBy-namberAy),2)))

print(f'Расстояние между точками = {long}')

