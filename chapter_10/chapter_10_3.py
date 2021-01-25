#3
class Information:
    def __init__(self, name, adress, age, number):
        self.name = name
        self.adress = adress
        self.age = age
        self.number = number

    def get_name(self):
        return self.name

    def get_adress(self):
        return self.adress

    def get_age(self):
        return self.age

    def get_number(self):
        return self.number

people_1 = Information('Vladislav', 'Lenina 22', 19, 7978)
people_2 = Information('Name_2', 'Octobers 33', 36, 7920)
people_3 = Information('Name_3', 'Tolstogo 36', 14, 7910)
