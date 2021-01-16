#8
def job():
    surface_area = float(input('Введите площадь поверхности окрашиваемой стены: '))
    paint_money = float(input('Цена емкости краски в литрах: '))
    result_paint = paints(surface_area, paint_money)
    result_time = times(surface_area)
    summa = result_paint + result_time
    print(f'Общая сумма равна: {summa}')

def paints(surface_area, paint_money):
    result_surface_area = surface_area / 10 
    result_paint = result_surface_area * 5
    print(f'Количество емкости краски в литрах: {result_paint}')
    summa_paint = paint_money * result_paint
    print(f'Стоимость краски: {summa_paint}')
    return summa_paint

def times(surface_area):
    result_surface_area = surface_area / 10 
    result_time = result_surface_area * 8
    print(f'Количество необохдимых часов: {result_time}')
    result_money = result_time * 2000
    print(f'Стоимость работ равна: {result_money}')
    return result_money
    
job()
