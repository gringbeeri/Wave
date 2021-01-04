#10
qty_bun = int(input('Количество булок: '))

sugar = 1.5/48
oil = 1/48
flour = 2.75/48

result_sugar = qty_bun * sugar
result_oil = qty_bun * oil
result_flour = qty_bun * flour

print(f'Количество стаканов сахара: {result_sugar}')
print(f'Количество стаканов масла: {result_oil}')
print(f'Количество стаканов муки: {result_flour}')