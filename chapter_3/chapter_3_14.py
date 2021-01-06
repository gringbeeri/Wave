#14
weight = float(input('Введите вашу массу: '))
growth = float(input('Введите ваш рост: '))
body_index = weight / (growth ** 2)
body_index = float('{:.1f}'.format(body_index))
print(body_index)

if body_index <= 18.5:
    print('Ваш индекс массы недостаточный')
elif body_index >= 18.5 and body_index <= 25:
    print('Ваш индекс массы оптимальный')
elif body_index > 25:
    print('Ваш индекс массы превышен')