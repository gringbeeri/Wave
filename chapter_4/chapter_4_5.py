#5
year = int(input('Введите количетсво лет: '))
month = 12
months = month * year
for fallout in range(year):
    qty_fallout = 0
    print('Номер года:',fallout+1)
    for fallout_month in range(month):
        print('Дождевые осадки', fallout_month + 1, 'месяц: ')
        fallout_rain = float(input('Введите количество дождевых осадков: '))
        qty_fallout += fallout_rain
        fallout_rain = float(input('Введите дождевые осадки на 2 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 3 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 4 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 5 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 6 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 7 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 8 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 9 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 10 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 11 месяц: '))
            qty_fallout += fallout_rain
            fallout_rain = float(input('Введите дождевые осадки на 12 месяц: '))
            qty_fallout += fallout_rain
print(f'Количество месяцев: {months}')
print(f'Общее количество дождевых осадков: {qty_fallout}')
result_fallout = qty_fallout / months
print(f'Средняя толщина осадков: {result_fallout}')
