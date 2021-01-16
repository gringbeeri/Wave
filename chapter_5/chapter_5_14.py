#14
for body_falls in range(1, 11):
    def falling_distance(body_falls):
        distance = 1/2 * 9.8 * body_falls ** 2
        print('Время\tКоличество метров')
        print(body_falls, '\t', distance)

    falling_distance(body_falls)
