class Station:     
    def __init__(self, name_station):         
        self.name_station = name_station         
        self.list_train = []      
        
    def take_train(self, train):         
        self.list_train.append(train)      
    
    def list_train(self):         
        return self.list_train      
    
    def list_train_type(self):         
        self.type_pass = 0         
        self.type_cargo = 0         
        for train in self.list_train:             
            if 'пассажирский' in train['type_wagons']:                 
                self.type_pass += 1             
            elif 'грузовой' in train['type_wagons']:                 
                self.type_cargo += 1                     
    
    def send_train(self, train):         
        self.list_train.remove(train)  

    def info(self):
	    return f"{self.name_station}"
    
class Route:     
    def __init__(self, start_station, end_station):         
        self.list_station = [start_station, end_station]    
    
    def add_station(self, station):         
        self.list_station.insert(1, station)      
    
    def delete_station(self, station):         
        self.list_station.remove(station)      
    
    def info(self):         
	    list_station = "\n".join(f'{station.info()}' for station in list_station)
	    list_station = f"Список станций составляет:\n{self.start_station.info()}\n{list_station}\n{self.end_station.info()}"
	    return list_station	      
        
class Train:     
    def __init__(self, number, type_wagons, qty_wagons):         
        self.number = number         
        self.type_wagons = type_wagons         
        self.qty_wagons = qty_wagons         
        self.speed = 0      
    
    def add_speed(self, speed):         
        self.speed += speed      
    
    def reduce_speed(self, speed):         
        self.speed -= speed      
        
    def show_speed(self):         
        return self.speed      
    
    def qty_wagons_train(self):         
        return self.qty_wagons          
    
    def attach_wagons(self):         
        if self.speed == 0:             
            self.qty_wagons = self.qty_wagons + 1         
        else:             
            print('Поезд движется, прицепка невозможна')              
            
    def unhook_wagons(self):         
        if self.speed == 0:             
            self.qty_wagons = self.qty_wagons - 1         
        else:             
            print('Поезд движется, отцепка невозможна')          
            
    def take_route(self, route):         
        self.route = route              
    
    # def move_next(self):     
    #     for station in self.route:  
    #         print(station)
    
    # def move_back(self):
    #     for station in self.route:
    #         print(station)
#--------------------------------------------------------------------------------------------------------------------------------# 
#Объекты класса "Станция"# 
station_1 = Station('Sevastopol') 
station_2 = Station('Simferopol') 
station_3 = Station('Yalta') 
station_4 = Station('Dzhankoy') 
station_5 = Station('Foros') 
station_6 = Station('Kerch')  
#--------------------------------------------------------------------------------------------------------------------------------# 
#Объекты класса "Маршрут"#
route_1 = Route(station_1.name_station, station_6.name_station) 
route_1.add_station(station_3.name_station) 
route_1.add_station(station_4.name_station) 
route_1.list_complete_stations() 
#--------------------------------------------------------------------------------------------------------------------------------# 
#Объекты класса "Поезд"# 
train_1 = Train('344', 'пассажирский', 13) 
train_2 = Train('255', 'грузовой', 36) 
train_3 = Train('7474', 'грузовой', 98) 
#--------------------------------------------------------------------------------------------------------------------------------# 
#--------------------------------------------------------------------------------------------------------------------------------# 
#--------------------------------------------------------------------------------------------------------------------------------# 
station_1.take_train(train_3.__dict__) 
station_1.take_train(train_2.__dict__) 
station_1.list_train_type() 
train_3.take_route(route_1.list_stations) 
print(train_3.__dict__) 
print(station_1.__dict__)
