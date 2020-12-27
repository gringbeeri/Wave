#12
number_shares_buy = float(input("Число купленных акций: "))
buy_shares = float(input("Сумма за покупку акции: "))
result_buy_shares = number_shares_buy * buy_shares
procent_shares_buy = 0.3
procent_buy = result_buy_shares * procent_shares_buy
result_buy = result_buy_shares - procent_buy
print(result_buy)

number_shares_sale = float(input("Число проданных акций: "))
sale_shares = float(input("Сумма за продажу акции: "))
result_sale_shares = number_shares_sale * sale_shares
procent_shares_sale = 0.3
procent_sale = result_sale_shares * procent_shares_sale
result_sale = result_sale_shares - procent_sale
print(result_sale)

result_shares = result_sale - result_buy
print(f'Итоговая сумма выигрыша: {result_shares}')