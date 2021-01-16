#4
lists =[]
for number in range(20):
    number = int(input('Введите числа: '))
    lists.append(number)
print(lists)
min_number = min(lists)
print(f'Минимальное число в списке: {min_number}')
max_number = max(lists)
print(f'Максимальное число в списке: {max_number}')
summa_number = sum(lists)
print(f'Сумма чисел в списке: {summa_number}')
average_number = sum(lists) / len(lists)
print(f'Среднее арифметическое число в списке: {average_number}')
