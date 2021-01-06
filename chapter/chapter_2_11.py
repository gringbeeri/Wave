#11
men = int(input("Количество учащихся мужского пола: "))
female = int(input("Количество учащихся женского пола: "))
qty = men + female
percent_men = (men / qty) * 100
print(f'Процентность мужского пола: {percent_men}')
percent_female = (female / qty) * 100
print(f'Процентность женского пола: {percent_female}')