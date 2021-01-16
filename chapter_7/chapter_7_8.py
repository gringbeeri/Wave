#8
file_boy = open(r'/home/vladislav/Рабочий стол/seven/boy.txt', 'r')
list_boy = []
file_girl = open(r'/home/vladislav/Рабочий стол/seven/girl.txt', 'r')
list_girl = []
for line_boy in file_boy:
    list_boy.append(str(line_boy.strip()))
for line_girl in file_girl:
    list_girl.append(str(line_girl.strip()))
user_name = input('Введите имя: ')
if user_name in list_boy:
    print('Да, такое имя входит в популярные - мужских имен!')
elif user_name in list_girl:
    print('Да, такое имя входит в популярные женских имен')
else:
    print('Нет, такого имени нету')
