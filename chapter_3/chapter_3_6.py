#6
day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))
print(f'{day}.{month}.{year}')

if day * int(month) == year:
    print('Ваш год волшебный!')
elif day > 31 or day < 0 or month > 12 or month < 0 or year < 0:
    print('Неверно введеный формат')
elif day * int(month) != year:
    print('Обычный год')



