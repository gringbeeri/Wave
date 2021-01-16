#6
def calories():
    grams_fat = float(input('Количетсво жиров: '))
    grams_carbohyd = float(input('Количество углеводов: '))
    fat(grams_fat)
    carbohyd(grams_carbohyd)

def fat(grams_fat):
    calories_fat = grams_fat * 9
    print(f'Количетсво калории от жиров: {calories_fat}')

def carbohyd(grams_carbohyd):
    calories_carbohyd = grams_carbohyd * 4
    print(f'Количетсво калории от углеводов: {calories_carbohyd}')

calories()
