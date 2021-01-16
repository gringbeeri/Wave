#3
def insure():
    sum = float(input('Введите стоимость строения: '))
    insurance(sum)

def insurance(sum):
    result = (sum / 100) * 80
    print(f'Необходимая сумма для страховки: {result}')

insure()
