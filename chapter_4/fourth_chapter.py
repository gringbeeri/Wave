#1
error = 0
while True:
    for errors in range(0, 5):
        errors = int(input('Введите количество ошибок за первый день: '))
        error += errors
        errors = int(input('Введите количество ошибок за второй день: '))
        error += errors
        errors = int(input('Введите количество ошибок за третий день: '))
        error += errors
        errors = int(input('Введите количество ошибок за четвертый день: '))
        error += errors
        errors = int(input('Введите количество ошибок за пятый день: '))
        error += errors
        break
    break
print(f'Количетсво ошибок за пять дней: {error}')

#2
calories = 4.2 
while True:
    for calorie in range(0, 5):
        calorie = input('Сжечь количетсво калорий за 10 минут? ')
        if calorie == 'да':
            calori = 10 * float(calories)
            print(f'Соженные калории равны: {calori}')
        calorie = input('Сжечь количетсво калорий за 15 минут? ')
        if calorie == 'да':
            calori = 15 * float(calories)
            print(f'Соженные калории равны: {calori}')
        calorie = input('Сжечь количетсво калорий за 20 минут? ')
        if calorie == 'да':
            calori = 20 * float(calories)
            print(f'Соженные калории равны: {calori}')
        calorie = input('Сжечь количетсво калорий за 25 минут? ')
        if calorie == 'да':
            calori = 25 * float(calories)
            print(f'Соженные калории равны: {calori}')
        calorie = input('Сжечь количетсво калорий за 30 минут? ')
        if calorie == 'да':
            calori = 30 * float(calories)
            print(f'Соженные калории равны: {calori}')
        break
    break
print(f'Всего сожженно калорий: {calori}')

#3
summa = int(input('Введите сумму на месяц: '))
while True:
    print('Введите ваш налог на землю: ')
    expenses = int(input('Сумма: '))
    print('Введите ваш налог на автомобиль: ')
    expenses += int(input('Сумма: '))
    print('Введите ваш налог на недвижимость: ')
    expenses += int(input('Сумма: '))
    break
if expenses > summa:
    result = summa - expenses
    print(f'Сумма превысила выделенный бюджет: {result}')
elif expenses < summa:
    result = summa - expenses
    print(f'Ваша сэкономленная сумма: {result}')

#4
time = int(input('Введите количество часов: '))
speed = int(input('Введите вашу скорость: '))

print('Время\tCкорость')
print('-------------')
for hour in range(1, time+1):
    result = hour * speed
    print(hour, '\t', result)

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

#6
for degrees in range(1, 21):
    degree = ((9 / 5) * degrees) + 32
    print('-------------')
    print('Градусы Цельсия\tГрадусы Фаренгейта')
    print(degrees, '\t', degree)

#7
days = int(input('Введите количество дней: '))

for day in (range(days)):
    money_day = day + 1.0
    rub = money_day / 100
    print('День\tЗарплата')
    print(day+1, '\t', money_day)
    print(f'Зарботная плата в рублях: {rub} RUB')

#8
summa = 0
while True:
    numbers = int(input('Введите положительные числа: '))
    summa += numbers 
    if numbers < 0:
        summa -= numbers
        break
print(summa)

#9 
for year in range(1, 26):
    ocean_rise = year * 1.6
    ocean_rises = float('{:.2f}'.format(ocean_rise))
    print('--------------------')
    print('Год\tПоднятие уровня')
    print(year, '\t', ocean_rises)

#10
pay = 45000
years = 5
year_pay = 0
for year in range(years):
    print('-------------------')
    print(f'Год:', year + 1)
    for semester in range(2):
        year_pay += pay * 0.015
        pays = year_pay + pay
        print(f'Семестер {semester +1}:',pays)

#11
weigth = float(input('Введите ваш вес: '))
months = 6
print(f'Ваш вес на данный момент: {weigth} килограмм')
print('Месяц \t  Вес')
for month in range(months):
    weigth = weigth - 1.5 
    print('--------------')
    print(f'Месяц {month + 1}: {weigth} - количество килограмм')
print(f'Ожидаемый вес через 6 месяцев: {weigth} килограмм')

#12
numbers = int(input('Введите число: '))
factorial = 1
for num in range(1, numbers+1):
    factorial *= num
print(factorial)

#13
qtys = int(input('Введите количество: '))
insrease = float(input('Процент увеличение: '))
days = int(input('Количество дней: '))

print('День \t Популяция')
for day in range(days):
    qtys += qtys * insrease 
    qtys = float('{:.6f}'.format(qtys))
    print(day+1, '\t', qtys)

#14
size = 7
for star in range(size):
    for stars in range(star, 7):
        print('*', end='')
    print()

#15
num_step = 6
for stars in range(1, num_step):
    print("#", end="")
    size = ""*stars
    print(size + "#")


       





