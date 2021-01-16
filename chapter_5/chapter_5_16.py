#16
appraisal_1 = int(input('Первая оценка: '))
appraisal_2 = int(input('Вторая оценка: '))
appraisal_3 = int(input('Третья оценка: '))
appraisal_4 = int(input('Четвертая оценка: '))
appraisal_5 = int(input('Пятая оценка: '))

def calc_average(appraisal_1, appraisal_2, appraisal_3, appraisal_4, appraisal_5):
    result = (appraisal_1 + appraisal_2 + appraisal_3 + appraisal_4 + appraisal_5) / 5
    print(f'Средний балл равен: {result}')
calc_average(appraisal_1, appraisal_2, appraisal_3, appraisal_4, appraisal_5)

def determine_grade(appraisal):    
    if appraisal <= 60:
        print('Оценка: F')
    elif appraisal >= 60 and appraisal <= 69:
        print('Оценка: D')
    elif appraisal >= 70 and appraisal <= 79:
        print('Оценка: C')
    elif appraisal >= 80 and appraisal <= 89:
        print('Оценка: B')
    elif appraisal >= 90:
        print('Оценка: A')
determine_grade(appraisal_1)
determine_grade(appraisal_2)
determine_grade(appraisal_3)
determine_grade(appraisal_4)
determine_grade(appraisal_5)
