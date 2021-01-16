#11 - 12
def numbers():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    summa_numbers(number_1, number_2)

def summa_numbers(number_1, number_2):
    summa = number_1 + number_2
    answer = int(input('Введите ответ: '))
    if answer == summa:
        print('Вы правильно сложили числа')
    else:
        print('Ответ не верный')

numbers()

