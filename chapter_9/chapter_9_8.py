#8
dict_1 = {} 
print('Добрый день что вы желаете сделать: ') 
print('1 - отыскать адрес электронной почты?') 
print('2 - добавить новое имя и электронную почту?') 
print('3 - изменить существующий адрес электронной почты?') 
print('4 - удалить существующее имя и адрес электронной почты? ') 
while True:
    answer = input('Ваш ответ: ') 
    if answer == '1':     
        names = input('Введите имя пользователя электронной почты: ')     
        if names in dict_1:         
            print(dict_1[names]) 
        else:
            print('Имя пользователя не найдено')
    elif answer == '2':      
        name = str(input('Введите ваше имя: '))      
        mail = str(input('Введите вашу почту: '))      
        dict_1[name] = mail 
        print(dict_1)
    elif answer == '3':     
        name = input('Введите имя пользователя электронной почты: ')     
        if name in dict_1:         
            mail = input('Введите необоходимое значение электронной почты: ')         
            dict_1[name] = mail 
            print(dict_1)
        else:
            print('Такой учетной записи не сущетсвует')
    elif answer == '4':     
        name = input('Введите имя которое необходимо удалить: ')     
        if name == name:         
            del dict_1[name]  
            print(dict_1)
    if answer == '0':     
        del dict_1['0']          
        break     
