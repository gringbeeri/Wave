#12
list_number = []
user_number = int(input('Введите число: '))
for number in range(2, user_number + 1):
    list_number.append(number)
print(f'Список всех чисел: {list_number}')
for numbers in list_number:
    def is_prime(numbers):
        for prime_number in range(2, numbers):
            if numbers % prime_number == 0:
                return False
        print(f'Простые числа: {numbers}')
    is_prime(numbers)
