#12
software = int(input('Введите число приобретенных пакетов: '))
software_money = 99

if software < 9:
    result = software * software_money
    print(f'Сумма за покупку без скидки: {result}$')
elif software >= 10 and software <= 19:
    summa = software * software_money
    discount = (summa * 10) // 100
    result = summa - discount
    print(f'Сумма за покупку со скидки: {result}$')
elif software >= 20 and software <= 49:
    summa = software * software_money
    discount = (summa * 20) // 100
    result = summa - discount
    print(f'Сумма за покупку со скидки: {result}$')
elif software >= 50 and software <= 99:
    summa = software * software_money
    discount = (summa * 30) // 100
    result = summa - discount
    print(f'Сумма за покупку со скидки: {result}$')
elif software >= 100:
    summa = software * software_money
    discount = (summa * 40) // 100
    result = summa - discount
    print(f'Сумма за покупку со скидки: {result}$')