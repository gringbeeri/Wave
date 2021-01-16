#6
def computation(number, lists=[]):
    lists = [2, 6, 8, 14, 9, 3, 99, 5, 7]
    lists.append(number)
    for numbers in lists:
        if number < numbers:
            print(numbers)

computation(6)
