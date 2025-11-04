import datetime


# Текущие дата и время
today = datetime.datetime.now()
print(f'Текущие дата и время: {today}.')

# День недели
weekday = today.isoweekday()
print(f'День недели: {weekday}.')

# Определение високосного года
if today.year % 4 == 0 and today.year % 100 == 0 or today.year % 400 == 0:
    print('Год является високосным.')
else:
    print('Год не является високосным.')

# Ввод даты пользователем
enter_date = input('Введите дату в формате год-месяц-день: ')


# Сколько времени осталось от текущей даты, до введенной пользователем
parsed_date = datetime.datetime.strptime(enter_date, '%Y-%m-%d')
different = parsed_date - today
print(f'До даты, введенной пользователем осталось: {different.days} дней')
hours = int(different.seconds / 3600)
minutes = int((different.seconds / 60) - hours * 60)
print(f'До даты, введенной пользователем осталось: {different.days} дней {hours} часов {minutes} минут')


