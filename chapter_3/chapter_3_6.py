#6
day = int(input('Введите день: '))
month = input('Введите месяц: ')
year = int(input('Введите год: '))
print(f'{day}.{month}.{year}')

if day * int(month) == year:
    print('Ваш год волшебный!')
else:
    print('Обычный год')