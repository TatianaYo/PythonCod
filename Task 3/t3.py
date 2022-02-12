# По заданному номеру дня недели вывести его название
print('Введите номер дня недели: ')
daynumber = int(input())

if daynumber == 1:
    print('Monday')
elif daynumber == 2:
    print('Tuesday')
elif daynumber == 3:
    print('Wednesday')
elif daynumber == 4:
    print('Thursday')
elif daynumber == 5:
    print('Friday')
elif daynumber == 6:
    print('Saturday')
elif daynumber == 7:
    print('Sunday')
else:
    print('Not found')
