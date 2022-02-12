# Показать последнюю цифру трёхзначного числа
print('Введите трехзначное число:')
a = int(input())
last_number = a % 10
print('Last number =', last_number)