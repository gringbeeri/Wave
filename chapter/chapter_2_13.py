#13
length_vines = float(input("Длина гряды в метрах: "))
volume_space_prop = float(input("Объем пространства, занимаемого концевой опорой в метрах: "))
volume_space_vines = float(input("Объем пространства между виноградными лозами в метрах: "))
result_vines = (length_vines - (2 * volume_space_prop)) / volume_space_vines
print(int('Количество виноградных лоз: {result_vines}'))
