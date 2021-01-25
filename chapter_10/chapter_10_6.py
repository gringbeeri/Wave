#6
class Patient:
    def __init__(self, name, patronymic, surname, adress, city, region, index, number, name_extr, number_extr):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.adress = adress
        self.city = city
        self.region = region
        self.index = index
        self.number = number
        self.name_extr = name_extr
        self.number_extr = number_extr

    def result_patient(self):
        result = self.name, self.patronymic, self.surname, self.adress, self.city, self.region, self.index, self.number, self.name_extr, self.number_extr
        return result

patient_1 = Patient('Vladislav', 'Andreevic', 'Gashko', 'October 22', 'Dzhankoy', 'Crimea', 219600, 7978, 'Name_1', 7980)
print(patient_1.result_patient())

class Procedure:
    def __init__(self, name_procedure, data_procedure, name_doctor, price_procedure):
        self.name_procedure = name_procedure
        self.data_procedure = data_procedure
        self.name_doctor = name_doctor
        self.price_procedure = price_procedure

    def result_procedure(self):
        result = f'Назание процедуры: \n {self.name_procedure} \n Дата: {self.data_procedure} \n Врач: {self.name_doctor} \n Стоимость: {self.price_procedure}'
        return result

procedure_1 = Procedure('Стоматолог', '22.12.2020', 'Ivan', 15.770)
procedure_2 = Procedure('Травматолог', '02.01.2021', 'Alex', 13.490)
procedure_3 = Procedure('Дерматолог', '12.01.2021', 'Denis', 2.270)
print(procedure_1.result_procedure())
print(procedure_2.result_procedure())
print(procedure_3.result_procedure())
