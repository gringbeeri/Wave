#12
number_shares_buy = 2000
buy_shares = 40.00
result_buy_shares = number_shares_buy * buy_shares
print(f'Сумма уплаченная за акции: {result_buy_shares}')
procent_shares_buy = 0.03
procent_buy = result_buy_shares * procent_shares_buy
print(f'Комиссия: {procent_buy}')
result_buy = result_buy_shares + procent_buy
print(f'Общая сумма уплаченная за акции: {result_buy}')

number_shares_sale = 2000
sale_shares = 42.75
result_sale_shares = number_shares_sale * sale_shares
print(f'Сумма уплаченная за акции: {result_sale_shares}')
procent_shares_sale = 0.03
procent_sale = result_sale_shares * procent_shares_sale
print(f'Комиссия: {procent_sale}')
result_sale = result_sale_shares - procent_sale
print(f'Общая сумма уплаченная за акции: {result_sale}')

result_shares = result_sale - result_buy
print(f'Итоговая сумма выигрыша: {result_shares}')
if result_shares > 0:
    print('Вы получили прибыль!')
elif result_shares < 0:
    print('Вы понесли убытки!')