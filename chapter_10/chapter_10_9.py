#9
dict_answer = {}
class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, number_answer):
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        self.number_answer = number_answer

    def dict_question(self, argument):
        result = {'1 ответ' : self.answer_1, '2 ответ' : self.answer_2, '3 ответ' : self.answer_3, '4 ответ' : self.answer_4, 'верный ответ' : self.number_answer}
        dict_answer[self.question] = result
    
    def players(self):
        self.qty_1 = 0
        self.qty_2 = 0
        print(question_1.question)
        print(f' 1.{question_1.answer_1} \n 2.{question_1.answer_2} \n 3.{question_1.answer_3} \n 4.{question_1.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_1.number_answer:
            self.qty_1 += 1
            print('Ответ верный')
        elif answer != question_1.number_answer:
            print('Неверный ответ')

        print(question_2.question)
        print(f' 1.{question_2.answer_1} \n 2.{question_2.answer_2} \n 3.{question_2.answer_3} \n 4.{question_2.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_2.number_answer:
            self.qty_1 += 1
            print('Ответ верный')
        elif answer != question_2.number_answer:
            print('Неверный ответ')

        print(question_3.question)
        print(f' 1.{question_3.answer_1} \n 2.{question_3.answer_2} \n 3.{question_3.answer_3} \n 4.{question_3.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_3.number_answer:
            self.qty_1 += 1
            print('Ответ верный')
        elif answer != question_3.number_answer:
            print('Неверный ответ')

        print(question_4.question)
        print(f' 1.{question_4.answer_1} \n 2.{question_4.answer_2} \n 3.{question_4.answer_3} \n 4.{question_4.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_4.number_answer:
            self.qty_2 += 1
            print('Ответ верный')
        elif answer != question_4.number_answer:
            print('Неверный ответ')
        
        print(question_5.question)
        print(f' 1.{question_5.answer_1} \n 3.{question_5.answer_2} \n 3.{question_5.answer_3} \n 4.{question_5.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_5.number_answer:
            self.qty_2 += 1
            print('Ответ верный')
        elif answer != question_5.number_answer:
            print('Неверный ответ')
    
        print(question_6.question)
        print(f' 1.{question_6.answer_1} \n 3.{question_6.answer_2} \n 3.{question_6.answer_3} \n 4.{question_6.answer_4}')
        answer = input('Введите ваш ответ: ')
        if answer == question_6.number_answer:
            self.qty_2 += 1
            print('Ответ верный')
        elif answer != question_6.number_answer:
            print('Неверный ответ')

    def result(self):
        if self.qty_1 > self.qty_2:
            print('Победил игрок 1')
        elif self.qty_1 < self.qty_2:
            print('Победил игрок 2')
        else:
            print('Ничья')
      

question_1 = Question('Столица России: ?', 'Москва', 'Берлин', 'Вена', 'Дортмунд', 'Москва')
question_2 = Question('Столица Украины: ?', 'Москва', 'Киев', 'Марсель', 'Ницца', 'Киев')
question_3 = Question('Столица Франции: ?', 'Анкара', 'Токио', 'Париж', 'Милан', 'Париж')
question_4 = Question('Столица Великобритании: ?', 'Барселона', 'Лондон', 'Мадрид', 'Пекин', 'Лондон')
question_5 = Question('Столица Испании: ?', 'Монако', 'Манчестер', 'Лион', 'Мадрид', 'Мадрид')
question_6 = Question('Столица Португалии: ?', 'Лиссабон', 'Рим', 'Копенгаген', 'Варшава', 'Лиссабон')

question_1.dict_question(question_1)
question_2.dict_question(question_2)
question_3.dict_question(question_3)
question_4.dict_question(question_4)
question_5.dict_question(question_5)
question_6.dict_question(question_6)

question_1.players()

question_1.result()
