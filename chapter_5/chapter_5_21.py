#21
import random
guess = random.randint(1, 10)
def random_number():
    counter = 0
    while True:
        number = int(input('Введите число: '))
        if number != guess:
            counter += 1
        if number == guess:
            print('Поздравляем, вы угадали!')
            break
        elif number < 0 or number > 10:
            print('Вы вышли за границы загаданного диапазона')
        elif number > guess:
            print('Слишком много, попробуйте еще раз!')
        elif number < guess:
            print('Слишком мало, попробуйте еще раз!')
    print(f'Количество попыток: {counter}')
random_number()
