#7
list_answer = []
list_answer_1 = []
new_list = []
file_answer = open(r'/home/vladislav/Рабочий стол/seven/gai.txt', 'r')
file_answer_1 = open(r'/home/vladislav/Рабочий стол/seven/gai_1.txt', 'r')

for line_answer in file_answer:
    list_answer.append(line_answer.strip())
for i, answer in enumerate(list_answer):
    print(f'{i + 1}. {answer}')

for line_answer_1 in file_answer_1:
    list_answer_1.append(line_answer_1.strip())
for v, answer_1 in enumerate(list_answer_1):
    print(f'{v + 1}. {answer_1}')

for gai in list_answer:
    if gai in list_answer_1:
        new_list.append(gai)
print(new_list)

