#3
lists = []
for months in range(12):
    month = float(input(f'Осадки за {months + 1} месяц: '))
    print(f'Количетсво осадков за {months + 1} месяц, равно: {month}')
    lists.append(month)
print(lists)
result_year = sum(lists)
print(f'Суммарное количетсво осадков за год: {result_year}')
result_month = sum(lists) / len(lists)
print(f'Среднее ежемесячное количество дождевых осадков: {result_month}')
result_max = max(lists)
print(f'Максимальное количетство осадков было с количеством: {result_max}')
result_min = min(lists)
print(f'Минимальное количетство осадков было с количеством: {result_max}')
