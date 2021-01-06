#10
summa = 0
first_try = int(input('Введите монету: '))
summa += first_try
second_try = int(input('Введите монету: '))
summa += second_try
third_try = int(input('Введите монету: '))
summa += third_try

if summa == 100:
    print(f'Достаточная сумма - {summa}')
elif summa < 100:
    print(f'Маленькая сумма - {summa}')
elif summa > 100:
    print(f'Большая сумма - {summa}')