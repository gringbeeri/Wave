#14
basic_summa = float(input("Внесенная основная сумма: "))
annual_rate = float(input("Годовая ставка: "))
frequency = int(input("Частота начисления суммы: "))
years = int(input("Количество лет: "))

result_summa = basic_summa * (1 + annual_rate / frequency) ** (frequency * years)
print(f'Итоговый баланс: {int(result_summa)}')
