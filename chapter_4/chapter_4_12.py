#12
numbers = int(input('Введите число: '))
factorial = 1
for num in range(1, numbers+1):
    factorial *= num
print(factorial)