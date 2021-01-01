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