#9 
for year in range(1, 26):
    ocean_rise = year * 1.6
    ocean_rises = float('{:.2f}'.format(ocean_rise))
    print('--------------------')
    print('Год\tПоднятие уровня')
    print(year, '\t', ocean_rises)