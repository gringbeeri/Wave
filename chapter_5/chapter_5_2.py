#2 
def tax():
    sum = float(input('Сумму покупок: '))
    print(f'Сумма покупок: {sum}')
    federal_tax = federal(sum)
    regional_tax = regional(sum)
    general_tax = federal_tax + regional_tax
    print(f'Общий налог: {general_tax}')
    result = sum - general_tax 
    print(f'Общая сумма продаж: {result}')

def federal(sum):
    result_federal = sum * 0.05
    print(f'Федеральный налог равен: {result_federal}')
    return result_federal

def regional(sum):
    result_regional = sum * 0.025
    print(f'Региональный налог равен: {result_regional}')
    return result_regional

tax()
