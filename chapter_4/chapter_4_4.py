#4
time = int(input('Введите количество часов: '))
speed = int(input('Введите вашу скорость: '))

print('Время\tCкорость')
print('-------------')
for hour in range(1, time+1):
    result = hour * speed
    print(hour, '\t', result)