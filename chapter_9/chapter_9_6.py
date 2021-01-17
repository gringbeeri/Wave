#6
file_word_1 = open(r'/home/vladislav/Рабочий стол/nine/file_6_1.txt', 'r')
file_word_2 = open(r'/home/vladislav/Рабочий стол/nine/file_6_2.txt', 'r')
list_1 = []
list_2 = []
myset_1 = set()
myset_2 = set()

for word_1 in file_word_1:
    list_1.append(word_1.strip())
    myset_1.update(list_1)
print(myset_1) 

for word_2 in file_word_2:
    list_2.append(word_2.strip())
    myset_2.update(list_2)
print(myset_2)

myset_3 = myset_1.intersection(myset_2)
print(myset_3)

myset_4 = myset_1.difference(myset_2)
print(myset_4)

myset_5 = myset_2.difference(myset_1)
print(myset_5)

myset_6 = myset_1.symmetric_difference(myset_2)
print(myset_6)
