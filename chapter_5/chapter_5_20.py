#20
current_amount = float(input('Введите текущую сумма на счету: '))
rate = float(input('Введите желаемую процентную ставку: '))
qty_month = int(input('Введите количество меяцев: '))

def count(current_amount, rate, qty_month):
    future_amount = current_amount * ((rate + qty_month) ** 2)
    print(f'Ваша будущая сумма после заданных параметров равна: {future_amount}')

count(current_amount, rate, qty_month)
