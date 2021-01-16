#1 
def distance():
    distance_km = float(input('Количество километров: '))
    miles(distance_km)

def miles(distance_km):
    mile = distance_km * 0.6214
    print(f'Количетсво миль: {mile}')

distance()
