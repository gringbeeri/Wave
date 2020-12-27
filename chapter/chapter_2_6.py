#6
money = float(input("Введите сумму средств: "))
print(money)
federal  = money * 0.05
print(federal)
regional = money * 0.025 
print(regional)
general_tax = federal + regional
print(general_tax)
result = money - general_tax
print(result)