#15
body_mass = float(input('Введите массу тела в килограммах: '))
speed = float(input('Количество метров в секунду: '))

def kinetic_energy(body_mass, speed):
    energy = 1/2 * body_mass * speed ** 2
    print(f'Кинетическая энергия равна: {energy}')

kinetic_energy(body_mass, speed)
