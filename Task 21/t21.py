# Программа проверяет пятизначное число на палиндромом.
string = input('Введите число: ')
reversed_string = ''.join(reversed(string))
if reversed_string == string:
    print(string," is Palindrome")
else:
    print("Not a Palindrome")
