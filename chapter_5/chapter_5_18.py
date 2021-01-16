#18
def is_prime(number):
    for numbers in range(2, number):
        if number % numbers == 0:
            return False
    return True
print(is_prime(9))
