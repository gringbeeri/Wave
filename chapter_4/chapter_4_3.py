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