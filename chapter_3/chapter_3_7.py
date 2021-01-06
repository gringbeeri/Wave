#7
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
