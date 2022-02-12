# Показать четные числа от 1 до N
a = 1
print('Enter b = ')
b = int(input())

while a < b:
    if a % 2 == 0:
        print(a)
    a += 1