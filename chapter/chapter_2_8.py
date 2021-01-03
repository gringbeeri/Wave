#8
summa = float(input("Введите сумму: "))
tip = summa * 0.18
print(f'Чаевые: {tip}')
tax = summa * 0.07
print(f'Налоговый сбор: {tax}')
summa_tax = tip + tax
result = summa + summa_tax
print(f'Итоговая сумма: {result}')
