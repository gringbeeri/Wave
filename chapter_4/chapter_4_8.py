#8
summa = 0
while True:
    numbers = int(input('Введите положительные числа: '))
    summa += numbers 
    if numbers < 0:
        summa -= numbers
        break
print(summa)