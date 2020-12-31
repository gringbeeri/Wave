# 10
summa = 0
first_try = int(input('Введите монету: '))
summa += first_try
second_try = int(input('Введите монету: '))
summa += second_try
third_try = int(input('Введите монету: '))
summa += third_try

if summa == 100:
    print(f'Достаточная сумма - {summa}')
elif summa < 100:
    print(f'Маленькая сумма - {summa}')
elif summa > 100:
    print(f'Большая сумма - {summa}')


17
internet = input('У вас плохое Wi-Fi соединение? ')

if internet == 'да':
    print('Пробовали перезагрузить устройство? ')
    internet = input('Ваш ответ: ')
    if internet == 'да':
        print('Хорошо, вытащите кабель интернета из порта роутера и снова вставьте, затем перезгрузите роутер! Решилось?')
        internet = input('Ваш ответ: ')
        if internet == 'нет':
            print('Рекомендуем заменить роутер')
        elif internet == 'да':
            print('Отлично, поздравляем')
    elif internet == 'нет':
        print('Перезагрузитесь пожалуйста')
elif internet == 'нет':
    print('Рады что все хорошо')

#18
vegetarians = ['Центральная пицерия', 'Кафе за углом', 'Блюдо от итальняской мамы', 'Кухня шеф-повар']
vegans = ['Кафе за углом', 'Кухня шеф-повар']
diets = ['Центральная пицерия', 'Кафе за углом', 'Кухня шеф-повар']
vegetarians_vegans = ['Кафе за углом', 'Кухня шеф-повар']
vegetarians_diets = ['Центральная пицерия', 'Кафе за углом', 'Кухня шеф-повар']
vegans_diets = ['Кафе за углом', 'Кухня шеф-повар']
vegetarians_vegans_diets = ['Центральная пицерия', 'Кафе за углом', 'Блюдо от итальняской мамы', 'Кухня шеф-повар']

vegetarian = input('Есть ли среди группы вегетарианцы? ')
vegan = input('Есть ли среди группы веганы? ')
diet = input('Есть ли среди группы люди с диетой? ')
if vegetarian == 'да' or vegan == 'да' and diet == 'нет':
    print('\n'.join(vegetarians_vegans))
elif vegetarians == 'да' and vegan == 'нет' or diet == 'да':
    print('\n'.join(vegetarians_diets))
elif vegetarians == 'нет' and vegan == 'да' or diet == 'да':
    print('\n'.join(vegans_diets))
elif vegetarians == 'да' and vegan == 'да' and diet == 'да':
    print('\n'.join(vegetarians_vegans_diets))

