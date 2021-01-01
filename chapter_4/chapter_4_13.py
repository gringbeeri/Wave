#13
qtys = int(input('Введите количество: '))
insrease = float(input('Процент увеличение: '))
days = int(input('Количество дней: '))

print('День \t Популяция')
for day in range(days):
    qtys += qtys * insrease 
    qtys = float('{:.6f}'.format(qtys))
    print(day+1, '\t', qtys)
