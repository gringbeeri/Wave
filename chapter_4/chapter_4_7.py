#7
days = int(input('Введите количество дней: '))

for day in (range(days)):
    money_day = day + 1.0
    rub = money_day / 100
    print('День\tЗарплата')
    print(day+1, '\t', money_day)
    print(f'Зарботная плата в рублях: {rub} RUB')