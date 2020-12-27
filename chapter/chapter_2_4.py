#4
product_1 = float(input("Сумма 1 товара: "))
product_2 = float(input("Сумма 2 товара: "))
product_3 = float(input("Сумма 3 товара: "))
product_4 = float(input("Сумма 4 товара: "))
product_5 = float(input("Сумма 5 товара: "))

summa = product_1 + product_2 + product_3 + product_4 + product_5
print(summa)
tax_summa = summa * 0.7
print(tax_summa)
result = summa + tax_summa
print(result)