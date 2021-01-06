#11
point = 0
books = int(input('Введите количество книг: '))

if books == 0:
    point += 0
    print(f'У вас {point} очков')
elif books == 2:
    point += 5
    print(f'У вас {point} очков')
elif books == 4:
    point += 15
    print(f'У вас {point} очков')
elif books == 6:
    point += 30
    print(f'У вас {point} очков')
elif books > 8:
    point += 60
    print(f'У вас {point} очков')
