#9
pocket = int(input('Введите номер кармана: '))

if pocket > 36:
    print('Ошибка')
elif pocket == 0:
    print('Карман зеленый')
elif pocket >= 1 and pocket <= 10:
    if pocket % 2 == 0:
        print('Карман черный')
    elif pocket % 2 != 0:
        print('Карман красный')
elif pocket >= 11 and pocket <= 18:
    if pocket % 2 == 0:
        print('Карман красный')
    elif pocket % 2 != 0:
        print('Карман черный')
elif pocket >= 19 and pocket <= 28:
    if pocket % 2 == 0:
        print('Карман черный')
    elif pocket % 2 != 0:
        print('Карман красный')
elif pocket >= 29 and pocket <= 36:
    if pocket % 2 == 0:
        print('Карман красный')
    elif pocket % 2 != 0:
        print('Карман черный')