#5
file_word = open(r'/home/vladislav/Рабочий стол/nine/file_5.txt', 'r')
dict_word = {}
for word in file_word:
    if word in dict_word:
        dict_word[word] += 1
    else:
        dict_word[word] = 1
print(dict_word) 
