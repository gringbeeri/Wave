#11
number_1 = int(input('1 число: '))
number_2 = int(input('2 число: '))
number_3 = int(input('3 число: '))
number_4 = int(input('4 число: '))
number_5 = int(input('5 число: '))
number_6 = int(input('6 число: '))
number_7 = int(input('7 число: '))
number_8 = int(input('8 число: '))
number_9 = int(input('9 число: '))
lists = [[f'{number_1}, {number_2}, {number_3}'],
         [f'{number_4}, {number_5}, {number_6}'],
         [f'{number_7}, {number_8}, {number_9}']]
def square(lists):
    summa = number_1 + number_2 + number_3
    if number_4 + number_5 + number_6 == summa and number_7 + number_8 + number_9 == summa and number_1 + number_5 + number_9 == summa:
        print('Квадрат соответвует квадрату Ло Шу')
    elif number_4 + number_5 + number_6 != summa and number_7 + number_8 + number_9 != summa:
        print('Квадрат не соответсвует квадрату Ло Шу')
    print(f'{number_1} | {number_2} | {number_3}','\n'
         f'{number_4} | {number_5} | {number_6}','\n'
         f'{number_7} | {number_8} | {number_9}')
square(lists)
