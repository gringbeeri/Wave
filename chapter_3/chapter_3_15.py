#15
seconds = int(input('Введите количество секунд: '))

if seconds >= 60 and seconds < 3599:
    minute = seconds // 60 
    ramainder_second = minute * 60
    second = seconds % ramainder_second
    print(f'{minute} минут, {second} секунд')

elif seconds >= 3600 and seconds < 86399:
    hours = (seconds // 60) // 60
    ramainder_minute = hours * 60 
    minute = seconds // 60
    minutes = minute % ramainder_minute
    ramainder_second = minute * 60
    seconds = seconds % ramainder_second
    print(f'{hours} часов, {minutes} минут, {seconds} секунд')

elif seconds >= 86400:
    days = ((seconds // 60) // 60) // 24
    ramainder_hour = days * 24
    hour = (seconds // 60) // 60
    hours = hour % ramainder_hour
    ramainder_minute = hours * 60
    minute = seconds // 60
    minutes = minute % ramainder_minute
    ramainder_second = minute * 60
    seconds = seconds % ramainder_second
    print(f'{days} дней, {hours} часов, {minutes} минут, {seconds} секунд')