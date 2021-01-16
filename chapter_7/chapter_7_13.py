#13
import random
list_ball = []
file_ball = open(r'/home/vladislav/Рабочий стол/seven/ball.txt', 'r')
for line in file_ball:
    list_ball.append(line.strip())
while True:
    question = input('Задайте вопрос: ')
    randoms = random.choice(list_ball)
    print(randoms)
    if question == 'выйти':
        break
    break

#14 Графика

#15 Графика
