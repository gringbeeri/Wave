#8
import math
qty_people = int(input('Количетсво участников: '))
qty_hot_gog = int(input('Количетсво хот-догов на человека: '))
sausage = 8
bun = 10

general_qty = qty_people * qty_hot_gog
print(f'Общее количество хот-догов: {general_qty}')
result_sausage = general_qty / sausage
qty_sausage = math.ceil(result_sausage) * sausage
print(f'Минимальное количество упаковок сосисок: {math.ceil(result_sausage)}')
result_bun = general_qty / bun
qty_bun = math.ceil(result_bun) * bun
print(f'Минимальное количество упаковок булок: {math.ceil(result_bun)}')
result_sausage_1 = qty_sausage % general_qty
print(f'Оставшиеся сосиски: {result_sausage_1}')
result_bun_1 = qty_bun % general_qty
print(f'Оставшиеся булки: {result_bun_1}')