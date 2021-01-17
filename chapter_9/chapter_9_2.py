#2
import random
list_country = []
count_true = 0
count_false = 0
dict_1 = {'США':'Вашингтон', 'Россия':'Москва', 'Испания':'Мадрид', 'Франция':'Париж', 'Украина':'Киев', 'Австрия':'Вена'}
for key in dict_1:
    list_country.append(key)
while True:
    country = random.choice(list_country)
    print(f'Страна: {country}')
    capital = input('Введите столицу страны: ')
    if capital == 'стоп':
        break
    if capital in dict_1[country]:
        print('Вы угадали столицу!')
        count_true += 1
        print(f'Количество угаданных попыток: {count_true}')
    else:
        print('Вы не угадали столицу...')
        count_false += 1
        print(f'Количество неугаданных попыток: {count_false}')
