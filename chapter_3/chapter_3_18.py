#18
vegetarians = ['Центральная пицерия', 'Кафе за углом', 'Блюдо от итальняской мамы', 'Кухня шеф-повар']
vegans = ['Кафе за углом', 'Кухня шеф-повар']
diets = ['Центральная пицерия', 'Кафе за углом', 'Кухня шеф-повар']
vegetarians_vegans = ['Кафе за углом', 'Кухня шеф-повар']
vegetarians_diets = ['Центральная пицерия', 'Кафе за углом', 'Кухня шеф-повар']
vegans_diets = ['Кафе за углом', 'Кухня шеф-повар']
vegetarians_vegans_diets = ['Центральная пицерия', 'Кафе за углом', 'Блюдо от итальняской мамы', 'Кухня шеф-повар']

vegetarian = input('Есть ли среди группы вегетарианцы? ')
vegan = input('Есть ли среди группы веганы? ')
diet = input('Есть ли среди группы люди с диетой? ')
if vegetarian == 'да' or vegan == 'да' and diet == 'нет':
    print('\n'.join(vegetarians_vegans))
elif vegetarians == 'да' and vegan == 'нет' or diet == 'да':
    print('\n'.join(vegetarians_diets))
elif vegetarians == 'нет' and vegan == 'да' or diet == 'да':
    print('\n'.join(vegans_diets))
elif vegetarians == 'да' and vegan == 'да' and diet == 'да':
    print('\n'.join(vegetarians_vegans_diets))