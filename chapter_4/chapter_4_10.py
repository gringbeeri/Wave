#10
pay = 45000
years = 5
year_pay = 0
for year in range(years):
    print('-------------------')
    print(f'Год:', year + 1)
    for semester in range(2):
        year_pay += pay * 0.015
        pays = year_pay + pay
        print(f'Семестер {semester +1}:',pays)