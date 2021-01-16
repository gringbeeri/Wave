#4
credit = float(input('Платеж по кредитам: '))
insurance = float(input('Сраховая стоимость: '))
petrol = float(input('Сумма бензина: '))
oil = float(input('Сумма масло: '))
tires = float(input('Сумма покупки шин: '))
service = float(input('Сумма за техобслуживания: '))
  
def months():
    result_month = credit + insurance + petrol + oil + tires + service
    print(f'Общая сумма за месяц: {result_month}')
    return result_month
months()

def years():
    result_years = (credit + insurance + petrol + oil + tires + service) * 12
    print(f'Общая сумма за месяц: {result_years}')
years()
