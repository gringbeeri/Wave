#5
body_mass = int(input('Введите массу тела: '))
body_weigh = body_mass * 9.8
print(body_weigh)

if body_weigh < 100:
    print('Слишком маленький вес')
elif body_weigh > 500:
    print('Слишком большой вес')
