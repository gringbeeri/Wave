#13
summa = 0
weight_package = int(input('Введите массу пакета: '))

if weight_package <= 200:
    summa = 150
    print(f'Сумма доставки равна: {summa}')
elif weight_package > 200 and weight_package < 599:
    summa = 300
    print(f'Сумма доставки равна: {summa}')
elif weight_package >= 600 and weight_package < 999:
    summa = 400
    print(f'Сумма доставки равна: {summa}')
elif weight_package >= 100:
    summa = 475
    print(f'Сумма доставки равна: {summa}')