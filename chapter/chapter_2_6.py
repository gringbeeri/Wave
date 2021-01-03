#6
cost = float(input("Введите сумму продажи: "))
print(cost)
federal_tax = cost * 0.05
print(f'Федеральный налог: {federal_tax}')
regional_tax = cost * 0.025 
print(f'Региональный налог: {regional_tax}')
general_tax = federal_tax + regional_tax
print(f'Общий налог с продаж: {general_tax}')
result = cost + general_tax
print(f'Сумма покупки: {cost}, общая сумма с продаж с учетом налога: {result}')