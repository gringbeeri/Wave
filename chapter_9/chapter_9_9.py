#9
import random
list_values_1 = []
list_values_2 = []
cart = {'two_pik' : 2, 'five_bubey' : 5, 'jack' : 10, 'lady' : 10,
        'king' : 10, 'ace_1' : 11, 'ace_2' : 1}
player_1 = 0
player_2 = 0
name_1 = 'vlad'
name_2 = 'lera'
for value in cart.values():
    list_values_1.append(value)
    list_values_2.append(value)
print(list_values_1)
print(list_values_2)


while True:
    deck_1 = random.choice(list_values_1)
    deck_2 = random.choice(list_values_2)
    if player_1 >= 21: 
        print(f'Победил игрок {name_1} с количетсвом карт {player_1}')
        break
    elif player_2 >= 21:
        print(f'Победил игрок {name_2} с количетсвом карт {player_2}')
        break
    print('Ходит игрок_1')
    map = input('Раздать еще карт? ')
    if map == 'да':
        print(deck_1)
    player_1 += deck_1
    if deck_1 == 11 or deck_1 == 1:
        player_1 -= deck_1
        if player_1 + deck_1 >= 50:
            player_1 += 1
        elif player_1 + deck_1 <= 50:
            player_1 += 11
    print(player_1)

    print('Ходит игрок 2')
    map = input('Раздать еще карт? ')
    if map == 'да':
        print(deck_2)
    player_2 += deck_2
    if deck_2 == 11 or deck_2 == 1:
        player_2 -= deck_2
        if player_2 + deck_2 >= 50:
            player_2 += 2
        elif player_2 + deck_2 <= 50:
            player_2 += 11
    print(player_2)
