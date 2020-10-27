print("Добрый день, заполните пожалуйста анкету: ")

database = []

my_age = []

dict_gender = {}

while True:
	start = input("Начать новый тест: ")
	if start == 'нет':
		break
	elif start == 'да':
		print("Поехали...")
	else:
		exit()
	
	package = {}
	
	name = input("Введите ваше имя: ")
	package['name'] = name
	age = int(input("Введите ваш возраст: "))
	package['age'] = age
	gender = input("Введите ваш пол: ")
	package['gender'] = gender

	def griting(gender):

		if gender == gender:
			print(f"Приятно познакомиться, {name}")

			if age >= 19 and age <= 27:
				print("Вы еще молоды...")
			elif age >= 28 and age <= 37:
				print("Вам стоит поторопиться с поиском...")
			elif age >= 38 and age <= 59:
				print("Не заморачивайтесь")

		# elif gender == 'мужской':
		# 	print(f"Здравствуйте, уважаемый {name}")

		# 	if age >= 19 and age <= 31:
		# 		print("Юнный парень вы еще молоды")
		# 	elif age >= 32 and age <= 52:
		# 		print("Вам стоит поторопиться с поиском...")
		# 	elif age >= 53 and age <= 59:
		# 		print("Расслабтесь, и отдыхайте")

		# else:
		# 	print("Привет незнакомец")

	griting(gender)

	def shutdown(age):

		if age > 0 and age <= 18:
			print("У нас можно принимать участие в 18 лет")
			exit()

		elif age >= 60:
			print("Наша программа работает до 60 лет")
			exit()

	shutdown(age)

	print(f'Спасибо {name}, теперь давайте обсудим ваше трудоустройство, скажите пожалуйста: ')

	job = input("Работаете ли вы где-то? ")
	package['place_of_work'] = job

	def employment(job):

		if job == "да":
			print(f"Отлично, {name}, перейдем далее")



		elif job == "нет":
			print("Тогда предлагаем вам трудоустроиться: ")

	employment(job)
			
	profession = ['экономическое', 'творческое', 'техническое']

	print(f"Предоставляем вам выбор: ")

	for index, direction in enumerate(profession):
		print(index + 1, direction)

	status = input("Ваш выбор: ")

	profession_1_list = ['экономист', 'финансист', 'бухгалтер']

	profession_2_list = ['писатель', 'сценарист', 'музыкант']

	profession_3_list = ['энергетик', 'технолог', 'сантехник']

	def show_professions(profession_1_list):

		for index, direction in enumerate(profession_1_list):
			print(index + 1, direction)

	if status == '1':
		package['direction'] = 'economic'
		print("Направление - экономическое: ")
		print("Неплохо, что именно предпочитаете? ")

		show_professions(profession_1_list)

		economic = input("Выбирайте что-то конкретное: ")

		if economic == '1':
			print("Хороший выбор, вы нашли свою работу!")
			package['profession'] = 'экономист'

		elif economic == '2':
			print("Отличный выбор, ваша профессия очень востребована!")
			package['profession'] = 'финансист'

		elif economic == '3':
			print("Неплохо, поздравляем с выбором!")
			package['profession'] = 'бухгалтер'

	elif status == '2':
		package['direction'] = 'creative'
		print("Направление - творческое: ")
		print("Хорошо, а ближе к какой проффесии? ")

		show_professions(profession_2_list)

		creation = input("Выбирайте что-то конкретное: ")

		if creation == '1':
			print("Отличная вакансия, поздравляем")
			package['profession'] = 'писатель'

		elif creation == '2':
			print("Одна из лучших проффесий мира")
			package['profession'] = 'сценарист'

		elif creation == '3':
			print("Отлично, очень интересная проффесия") 
			package['profession'] = 'музыкант'

	elif status == '3':
		package['direction'] = 'technical'
		print("Направление - техническое: ")
		print("Хороший выбор, что из этого направления нравится? ")

		show_professions(profession_3_list)

		technical = input("Выбирайте что-то конкретное: ")

		if technical == '1':
			print("Хорошая, высокооплачиваемая проффесия")
			package['profession'] = 'энергетик'

		elif technical == '2':
			print("Мощная, нелегкая вакансия")
			package['profession'] = 'технолог'

		elif technical == '3':
			print("Отличный выбор, известная вакансия") 
			package['profession'] = 'сантехник'

	my_age.append(age)
	average = sum(my_age) // len(my_age)
	
	database.append(package)
	print(package)

for quantity in database:

	gender = quantity['gender']

	if gender in dict_gender:

		dict_gender[gender] += 1

	else:

		dict_gender[gender] = 1

print(dict_gender)

print(f' Средний возраста анкет составляет:', average,'%')
print(database)








	













