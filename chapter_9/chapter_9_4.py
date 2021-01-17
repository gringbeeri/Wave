#4
file_word = open(r'/home/vladislav/Рабочий стол/nine/file_4.txt', 'r')
myset = set()
list_word = []
for word in file_word:
    list_word.append(word.strip())
    myset.update(list_word)
print(myset)
