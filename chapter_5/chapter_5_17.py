#17
import random
even_number = []
odd_number = []
def random_numbers():
    for numbers in range(1, 101):
        number = random.randint(1, 1000)
        if number % 2 == 0:
            even_number.append(numbers)
        else:
            odd_number.append(numbers)
    print(f'Количество четных чисел: {len(even_number)}')
    print(f'Количество нечетных чисел: {len(odd_number)}')

random_numbers()
