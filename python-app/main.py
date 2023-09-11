import calendar

print('Добро пожаловать в календарь\n')

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))

print('Пока')