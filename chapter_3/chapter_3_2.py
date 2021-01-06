#2
len_triangle_1 = int(input('Введите длину: '))
width_triangle_1 = int(input('Введите ширину: '))
result_1 = len_triangle_1 * width_triangle_1
print(f'Площадь треугольника равна: {result_1}')

len_triangle_2 = int(input('Введите длину: '))
width_triangle_2 = int(input('Введите ширину: '))
result_2 = len_triangle_2 * width_triangle_2
print(f'Площадь треугольника равна: {result_2}')

if result_1 > result_2:
    print('Площадь первого треугольника больше')
elif result_1 < result_2:
    print('Площадь второго треугольника больше')
else:
    print('Стороны равны')