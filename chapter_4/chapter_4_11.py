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