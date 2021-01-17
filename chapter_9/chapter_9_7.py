#7
file_word = open(r'/home/vladislav/Рабочий стол/nine/file_7.txt', 'r')
file_year = open(r'/home/vladislav/Рабочий стол/nine/file_7_1.txt', 'r')
list_campion = []
dict_team = {}
list_year = []


for champion in file_word:
    list_campion.append(champion.strip())
for team in list_campion:
    if team in list_campion:
        count = list_campion.count(team)
        dict_team[team] = count
print(dict_team)

for year in file_year:
    list_year.append(year.strip())
dict_team_year = dict(zip(list_year, list_campion))
if '1904' and '1914' in dict_team_year:
    dict_team_year['1904' and '1914'] = '0'
print(dict_team_year)

year = str(input('Введите год: '))
if year in dict_team_year:
    print(dict_team_year[year])
