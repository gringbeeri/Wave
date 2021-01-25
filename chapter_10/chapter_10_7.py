#7
dict_people = {}
class Employee:
    def __init__(self, name, id_number, departament, position):
        self.name = name
        self.id_number = id_number
        self.departament = departament
        self.position = position
    
    def people_search(self, man):
        man = {'Имя' : self.name, 'Отдел' : self.departament, 'Должность' : self.position} 
        dict_people[self.id_number] = man

employee_1 = Employee('Vladislav', 4474, 'информационный', 'генеральный секретарь')
employee_2 = Employee('Dmitriy', 44736, 'информационный', 'заместитель министра')
employee_3 = Employee('Andrey', 44254, 'информационный', 'управляющий')

employee_1.people_search(employee_1)
employee_2.people_search(employee_2)
employee_3.people_search(employee_3)

def search_people():
    print('Меню:')
    print('1 - Найти контактное лицо')
    print('2-  Добавить новое контактное лицо')
    print('3 - Изменить существующее контактное лицо')
    print('4 - Удалить контактное лицо')
    print('5 - Выйти из программы')
    choice = int(input('Введите ваш выбор: '))
    if choice == 1:
        id_code = int(input('Введите ваш персональный код: '))
        if id_code in dict_people:
            print(dict_people.get(id_code, 'Это имя не найдено'))
    elif choice == 2:
        id_code = int(input('Введите выбранный код: '))
        if id_code not in dict_people:
            name = input('Введите ваше имя: ')
            departament = input('Введите название отдела: ')
            position = input('Введите вашу должность: ')
            man = {'Имя' : name, 'Отдел' : departament, 'Должность' : position}
            dict_people[id_code] = man
            print(dict_people)
    elif choice == 3:
        id_code = int(input('Введите ваш персональный код: '))
        if id_code in dict_people:
            name = input('Введите ваше имя: ')
            departament = input('Введите название отдела: ')
            position = input('Введите вашу должность: ')
            man = {'Имя' : name, 'Отдел' : departament, 'Должность' : position}
            dict_people[id_code] = man
            print(dict_people)
    elif choice == 4:
        id_code = int(input('Введите выбранный код: '))
        if id_code in dict_people:
            del(dict_people[id_code])
            print('Запись удалена')
            print(dict_people)
    elif choice == 5:
        print('Вы вышли из программы')  

search_people()
