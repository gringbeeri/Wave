#9
def sales_tax():
    volume_tax = float(input('Введите объем продаж за месяц: '))
    federal = federal_tax(volume_tax)
    municipal = municipal_tax(volume_tax)
    result_tax = federal + municipal
    print(f'Общий налог составляет: {result_tax}')

def federal_tax(volume_tax):
    result = volume_tax * 0.05
    print(f'Федеральный налог составляет: {result}')
    return result

def municipal_tax(volume_tax):
    result = volume_tax * 0.025
    print(f'Муниципальный налог составляет: {result}')
    return result

sales_tax()
