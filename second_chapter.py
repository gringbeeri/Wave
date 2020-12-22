#1
name = input("Введите ваше имя: ")
city = input("Введите ваш город: ")
region = input("Введите ваш регион ")
index = int(input("Введите ваш индекс: "))
number = int(input("Введите ваш номер телефона: "))
specialty = input("Введите вашу специальность: ")

print(f"Вас зовут {name}")
print(f"Вы проживаете в городе {city}, {region} область, ваш почтовый индекс: {index}")
print(f"Ваш номер телефона: {number}")
print(f"Ваша специальность: {specialty}")

#2
summa = int(input("Введите сумму: "))
result = (summa * 23) / 100
print(result)

#3
quantity = int(input("Введите количество квадратных метров: "))
result = quantity / 4047
print(result)

#4
product_1 = int(input("Сумма 1 товара: "))
product_2 = int(input("Сумма 2 товара: "))
product_3 = int(input("Сумма 3 товара: "))
product_4 = int(input("Сумма 4 товара: "))
product_5 = int(input("Сумма 5 товара: "))

summa = product_1 + product_2 + product_3 + product_4 + product_5
print(summa)
tax_summa = (summa * 7) // 100
print(tax_summa)
result = summa + int(tax_summa)
print(result)

#5
speed = 70
distance_1 = speed * 6
print(distance_1)
distance_2 = speed * 10
print(distance_2)
distance_3 = speed * 15
print(distance_3)

#6
money = int(input("Введите сумму средств: "))
print(money)
federal  = (money * 5) // 100
print(federal)
regional = (money * 2.5) // 100
print(int(regional))
general_tax = federal + int(regional)
print(general_tax)
result = money - general_tax
print(result)

#7
kilometers = int(input("Введите число пройденного пути: "))
petrol = float(input("Количество литров: "))
result = kilometers // petrol
print(result)

#8
summa = float(input("Введите сумму: "))
print(summa)
tip = (summa * 18) // 100
print(tip)
tax = (summa * 7) // 100
print(tax)
summa_tax = tip + tax
print(summa_tax)
result = summa - summa_tax
print(result)

#9
temperature = int(input("Введите температуру: "))
temperature_F = int(((9 / 5) * temperature) + 32)
print(temperature_F)

#10


#11
men = int(input("Количество учащихся мужского пола: "))
female = int(input("Количество учащихся мужского пола: "))
qty = men + female
percent_men = men // qty
print(percent_men)
percent_female = female // qty
print(percent_female)

#12
number_shares_buy = int(input("Число купленных акций: "))
buy_shares = float(input("Сумма за покупку акции: "))
result_buy_shares = number_shares_buy * buy_shares
procent_shares_buy = 3
procent_buy = (result_buy_shares * procent_shares_buy) // 100
result_buy = result_buy_shares - procent_buy
print(int(result_buy))

number_shares_sale = int(input("Число проданных акций: "))
sale_shares = float(input("Сумма за продажу акции: "))
result_sale_shares = number_shares_sale * sale_shares
procent_shares_sale = 3
procent_sale = (result_sale_shares * procent_shares_sale) // 100
result_sale = result_sale_shares - procent_sale
print(int(result_sale))

result_shares = result_sale - result_buy
print(f'Итоговая сумма выигрыша: {result_shares}')

#13
length_vines = float(input("Длина лоз: "))
volume_space_prop = float(input("Объем пространства опор: "))
volume_space_vines = float(input("Объем пространства лоз: "))
result_vines = (length_vines - 2) * volume_space_prop)) / volume_space_vines
print(int('Количество виноградных лоз: {result_vines}'))

#14
basic_summa = float(input("Внесенная основная сумма: "))
annual_rate = float(input("Годовая ставка: "))
frequency = int(input("Частота начисления суммы: "))
years = int(input("Количество лет: "))

result_summa = basic_summa * ((1 + (annual_rate / frequency)) ** 2)
print(f'Итоговый баланс: {int(result_summa)}')

#15
#Черепашья графика - я пока выполняю только по коду, графику изучу позже - если можно.






