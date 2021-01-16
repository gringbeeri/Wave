#5
def appraisal(cost_property):
    print(f'Фактическая стоимость недвижимости: {float(cost_property)}')
    appraisal_cost = (cost_property / 100) * 60
    print(f'Оценочная стоимость недвижимого имущества: {appraisal_cost}')
    cent = (appraisal_cost / 100)
    tax = 0.72 * cent
    tax_property = ("%.2f" % tax)
    print(f'Налог на имущества равен: {tax_property}')
appraisal(10000)
