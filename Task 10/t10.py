# Показать вторую цифру трёхзначного числа
print('Введите трехзначное число:')
a = int(input())
middle_num = ((a % 100 - a % 10) // 10)
print('Second number =', middle_num)