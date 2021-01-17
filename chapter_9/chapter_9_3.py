#3
file_code = open(r'/home/vladislav/Рабочий стол/nine/file_3.txt', 'r')
file_values = open(r'/home/vladislav/Рабочий стол/nine/file_3_1.txt', 'r')
list_1 = []
for key in file_code:
    list_1.append(key.strip())
list_2 = []
for value in file_values:
    list_2.append(value.strip())

dict_code = dict(zip(list_1, list_2))
print(dict_code)
