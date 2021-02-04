class Station:
    def __init__(self, name_station):
        self.name_station = name_station
        self.list_train = []
        self.type_pass = 0
        self.type_cargo = 0

    def take_train(self, train):
        self.list_train.append(train.__dict__)

    def list_train(self):
        return self.list_train

    def list_train_type(self):
        for train in self.list_train:
            if 'пассажирский' in train['type_train']:
                self.type_pass += 1
            elif 'грузовой' in train['type_train']:
                self.type_cargo += 1
               
    def send_train(self, train):
        self.list_train.remove(train)

class Route:
    def __init__(self, start_station, end_station, list_stations=[]):
        self.list_stations = []
        self.start_station = start_station
        self.list_station = []
        self.end_station = end_station

    def add_station(self, station):
        self.list_station.append(station)

    def delete_station(self, station):
        self.list_station.remove(station)

    def list_complete_stations(self):
        route_stations = {'start_station' : self.start_station, 'list_station' : self.list_station, 'end_station' : self.end_station}
        self.list_stations.insert(0, self.start_station)
        for additional in self.list_station:
            self.list_stations.append(additional)
        self.list_stations.append(self.end_station)

    def info(self):
        for each_station in self.list_stations:
            print(''.join(each_station))
     
class Train:
    def __init__(self, number_train, type_train, qty_wagons):
        self.number_train = number_train
        self.type_train = type_train
        self.qty_wagons = qty_wagons
        self.speed = 0
        self.route = []
        self.station = 0

    def add_speed(self, speed):
        self.speed += speed

    def reduce_speed(self, speed):
        self.speed -= speed

    def show_speed(self):
        return self.speed

    def qty_wagons_train(self):
        return self.qty_wagons
    
    def attach_wagons(self, wagon):
        if self.speed == 0:
            self.qty_wagons = self.qty_wagons + wagon
        else:
            print('Поезд движется, прицепка невозможна')
        
    def unhook_wagons(self, wagon):
        if self.speed == 0:
            self.qty_wagons = self.qty_wagons - wagon
        else:
            print('Поезд движется, отцепка невозможна')
    
    def take_route(self, route):
        self.route.append(route)
        self.station = route[0]
        
    def move_next(self):
        for station in self.route:
            self.station = station[0]
        if self.station == station[0]:
            del station[0]
    
    def move_back(self):
        # for station in self.route:
        #     # print(self.route)
        #     self.station = station[0]
        #     if self.station == station[0]:
        #         station.append([])

#--------------------------------------------------------------------------------------------------------------------------------#
#Объекты класса "Станция"
station_1 = Station('Sevastopol')
station_2 = Station('Simferopol')
station_3 = Station('Yalta')
station_4 = Station('Dzhankoy')
station_5 = Station('Foros')
station_6 = Station('Kerch')

#--------------------------------------------------------------------------------------------------------------------------------#
#Объекты класса "Маршрут"
route_1 = Route(station_1, station_6)
route_1.add_station(station_3)
route_1.add_station(station_4)
route_1.list_complete_stations()
#--------------------------------------------------------------------------------------------------------------------------------#
#Объекты класса "Поезд"
train_1 = Train('344', 'пассажирский', 13)
train_2 = Train('255', 'грузовой', 36)
train_3 = Train('7474', 'грузовой', 98)
#--------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#
station_1.take_train(train_3)
train_3.take_route(route_1.list_stations)
print(train_3.__dict__)
train_3.move_next()
print(train_3.__dict__)
train_3.move_next()
print(train_3.__dict__)
train_3.move_next()
print(train_3.__dict__)