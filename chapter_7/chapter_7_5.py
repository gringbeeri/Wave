#5
file_charge = open(r'/home/vladislav/Рабочий стол/seven/charge.txt', 'r')
list_charge = []

for charge in file_charge:
    list_charge.append(int(charge))
print(list_charge)

user_charge = int(input('Введите значение: '))

if user_charge in list_charge:
    print('Номер допустимый')
else:
    print('Номер недопустимый')
