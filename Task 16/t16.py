# Дано число обозначающее день недели. Выяснить является номер дня недели выходным
import random
a = random.randint(1, 7)
print(a)

if a == 6 or a == 7:
    print('Выходной')
else:
    print('Будни')