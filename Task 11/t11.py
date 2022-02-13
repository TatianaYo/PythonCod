# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
a = random.randint(10, 99)
print(a)
dig1 = a // 10
dig2 = a % 10

if dig1 > dig2:
    print('max =', dig1)
else:
    print('max =', dig2)
