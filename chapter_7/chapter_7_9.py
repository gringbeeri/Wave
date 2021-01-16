#9
def qty():
    file_qty = open(r'/home/vladislav/Рабочий стол/seven/qty.txt', 'r')
    list_qty = []
    for qty in file_qty:
        list_qty.append(int(qty))
    result_average = sum(list_qty) / len(list_qty)
    print(f'Среднее годовое изменение: {result_average}')
    result_max = max(list_qty)
    print(f'Максимальный прирост численности за весь период: {result_max}')
    result_min = min(list_qty)
     print(f'Минимальный прирост численности за весь период: {result_min}')

qty()
