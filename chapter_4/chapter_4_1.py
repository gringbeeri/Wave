#1
error = 0
while True:
    for errors in range(0, 5):
        errors = int(input('Введите количество ошибок за первый день: '))
        error += errors
        errors = int(input('Введите количество ошибок за второй день: '))
        error += errors
        errors = int(input('Введите количество ошибок за третий день: '))
        error += errors
        errors = int(input('Введите количество ошибок за четвертый день: '))
        error += errors
        errors = int(input('Введите количество ошибок за пятый день: '))
        error += errors
        break
    break
print(f'Количетсво ошибок за пять дней: {error}')