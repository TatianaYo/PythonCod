# Найти расстояние между точками в пространстве 2D/3D

xA = float(input("Введите координату xA: "))
yA = float(input("Введите координату yA: "))
zA = float(input("Введите координату zA: "))
xB = float(input("Введите координату xB: "))
yB = float(input("Введите координату yB: "))
zB = float(input("Введите координату zB: "))

x = xB - xA
y = yB - yA
z = zB - zA
from math import sqrt
dis2D = sqrt((x ** 2) + (y ** 2))
dis3D = sqrt((x ** 2) + (y ** 2) + (z ** 2))
print(dis2D, dis3D)