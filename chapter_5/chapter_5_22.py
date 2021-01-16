#22
import random 
stone = 'камень' 
scissors = 'ножницы' 
paper = 'бумага' 
number = random.randint(1, 3) 
if number == 1:     
    stone 
elif number == 2:     
    scissors 
elif number == 3:     
    paper 
print(number) 
def choises(choice):   
    choice = input('Введите ваш вариант: ') 
    if choice == 'камень' and number == 2:     
        print('Вы выиграли, камень победил!') 
    elif choice == 'камень' and number == 3:     
        print('Вы проиграли, бумага победила') 
    elif choice == 'ножницы' and number == 3:     
        print('Вы выиграли, ножницы победили!') 
    elif choice == 'ножницы' and number == 1:     
        print('Вы проиграли, камень побеждает') 
    elif choice == 'бумага' and number == 1:     
        print('Вы выиграли, бумага побеждает!') 
    elif choice == 'бумага' and number == 2:     
        print('Вы проиграли, ножницы побеждают')
choices(choise)
