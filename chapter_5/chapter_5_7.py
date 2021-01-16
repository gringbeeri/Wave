#7
def tickets():
    class_A = int(input('Количество проданных билетов класса А: '))
    class_B = int(input('Количество проданных билетов класса B: '))
    class_C = int(input('Количество проданных билетов класса C: '))
    row_A(class_A)
    row_B(class_B)
    row_C(class_C)

def row_A(class_A):
    result_A = class_A * 20
    print(f'Доход от продажи билетов класса А: {result_A}$')

def row_B(class_B):
    result_B = class_B * 20
    print(f'Доход от продажи билетов класса А: {result_B}$')

def row_C(class_C):
    result_C = class_C * 20
    print(f'Доход от продажи билетов класса А: {result_C}$')

tickets()

