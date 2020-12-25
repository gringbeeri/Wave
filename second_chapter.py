#1
number = int(input('Введите число: '))

if number == 1:
    print('Понедельник')
elif number == 2:
    print('Вторник')
elif number == 3:
    print('Среда')
elif number == 4:
    print('Четверг')
elif number == 5:
    print('Пятница')
elif number == 6:
    print('Суббота')
elif number == 7:
    print('Воскресенье')
else:
    print('Такого дня не сущетсвует!')

#2
len_triangle_1 = int(input('Введите длину: '))
width_triangle_1 = int(input('Введите ширину: '))
result_1 = len_triangle_1 * width_triangle_1
print(f'Площадь треугольника равна: {result_1}')

len_triangle_2 = int(input('Введите длину: '))
width_triangle_2 = int(input('Введите ширину: '))
result_2 = len_triangle_2 * width_triangle_2
print(f'Площадь треугольника равна: {result_2}')

if result_1 > result_2:
    print('Площадь первого треугольника больше')
elif result_1 < result_2:
    print('Площадь второго треугольника больше')
else:
    print('Стороны равны')

#3
age = float(input("Введите ваш возраст: "))

if age <= 1:
    print('Младенец')
elif age > 1 and age <= 13:
    print('Ребенок')
elif age > 13 and age < 20:
    print('Подросток')
else:
    print('Взрослый')

#4
numbers = int(input('Введите число: '))

if numbers == 1:
    print('I')
elif numbers == 2:
    print('II')
elif numbers == 3:
    print('III')
elif numbers == 4:
    print('IV')
elif numbers == 5:
    print('V')
elif numbers == 6:
    print('VI')
elif numbers == 7:
    print('VII')
elif numbers == 8:
    print('VIII')
elif numbers == 9:
    print('IX')
elif numbers == 10:
    print('X')
else:
    print('Не существует')

#5
body_mass = int(input('Введите массу тела: '))
body_weigh = body_mass * 9.8
print(body_weigh)

if body_weigh < 100:
    print('Слишком маленький вес')
elif body_weigh > 500:
    print('Слишком большой вес')

#6
day = int(input('Введите день: '))
month = input('Введите месяц: ')
year = int(input('Введите год: '))
print(f'{day}.{month}.{year}')

if day * int(month) == year:
    print('Ваш год волшебный!')
else:
    print('Обычный год')

# 7
first_color = input('Введите первый цвет: ')
second_color = input('Введите второй цвет: ')

if first_color == 'красный' and second_color == 'синий':
    print('Фиолетовый')
elif first_color == 'желтый' and second_color == 'красный':
    print('Оранжевый')
elif first_color == 'синий' and second_color == 'желтый':
    print('Зеленый')
else:
    print('Неверные цвета')

8
import math
qty_people = int(input('Количетсво участников: '))
qty_hot_gog = int(input('Количетсво хот-догов на человека: '))
sausage = 8
bun = 10

general_qty = qty_people * qty_hot_gog
print(f'Общее количество хот-догов: {general_qty}')
result_sausage = general_qty / sausage
qty_sausage = math.ceil(result_sausage) * sausage
print(f'Минимальное количество упаковок сосисок: {math.ceil(result_sausage)}')
result_bun = general_qty / bun
qty_bun = math.ceil(result_bun) * bun
print(f'Минимальное количество упаковок булок: {math.ceil(result_bun)}')
result_sausage_1 = qty_sausage % general_qty
print(f'Оставшиеся сосиски: {result_sausage_1}')
result_bun_1 = qty_bun % general_qty
print(f'Оставшиеся булки: {result_bun_1}')

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


#11
point = 0
books = int(input('Введите количество книг: '))

if books == 0:
    point += 0
    print(f'У вас {point} очков')
elif books == 2:
    point += 5
    print(f'У вас {point} очков')
elif books == 4:
    point += 15
    print(f'У вас {point} очков')
elif books == 6:
    point += 30
    print(f'У вас {point} очков')
elif books > 8:
    point += 60
    print(f'У вас {point} очков')

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

#14
weight = float(input('Введите вашу массу: '))
growth = float(input('Введите ваш рост: '))
body_index = weight / (growth ** 2)
body_index = float('{:.1f}'.format(body_index))
print(body_index)

if body_index <= 18.5:
    print('Ваш индекс массы недостаточный')
elif body_index >= 18.5 and body_index <= 25:
    print('Ваш индекс массы оптимальный')
elif body_index > 25:
    print('Ваш индекс массы превышен')

#15
# time = int(input('Введите количество секунд: '))
# minute = time // 60 
# hour = time * 60 * 60
# day = 24 * 60 * 60

# if time >= 60 and time < 3599:
#     minute = time // 60 
#     second = minute % 60
#     print(f'{minute} минут, {second} секунд')
# elif time >= 3600 and time < 86399:
#     hour = second * 60 * 60
#     print(f'{hour} часов, {minute} минут, {tume} секунд')
# elif time >= 86400:
#     print(f'{day} дня, {hour} часов, {minute} минут, {time} секунд')

16
year = int(input('Введите год: '))

if year % 100 == 0 and year % 400 == 0:
    print(f'В {year} году, в феврале было 29 дней')
elif year % 100 != 0 and year % 4 == 0:
    print(f'В {year} году, в феврале было 29 дней')
else:
    print(f'{year} - год не високосный')

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
