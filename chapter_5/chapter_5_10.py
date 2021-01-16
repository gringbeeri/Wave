#10
def inches():
    feet = int(input('Введите количество футов: '))
    feet_to_inches(feet)

def feet_to_inches(feet):
    result = feet * 12
    print(f'Количество дюймов равно: {result}')

inches()

