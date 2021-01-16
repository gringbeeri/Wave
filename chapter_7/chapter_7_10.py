#10
file_team = open(r'/home/vladislav/Рабочий стол/seven/team.txt', 'r')
list_team = []
for team in file_team:
    list_team.append(team.strip())
user_team = input('Введите команду: ')
if user_team in list_team:
    count = list_team.count(user_team)
    print(f'Эта команда побеждала в течении: {count} лет')
else:
    print('Команда не побеждала в выбранный период лет')
