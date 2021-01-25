#2
class Car:
    def __init__(self, year_model, make, speed=0):
        self.year_model = year_model
        self.make = make
        self.speed = 0
    
    def accelerate_speed(self, speed=5):
        self.speed += 5

    def break_speed(self, speed=5):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed

car_1 = Car('w221', 'Mercedes-Benz')
car_1.accelerate_speed()
car_1.accelerate_speed()
car_1.break_speed()
car_1.break_speed()
print(car_1.get_speed())
