import datetime
#Ввод даты
year, month, day = map(int, input('date: ').split())
d = datetime.date(year,month,day)
#Ввод количества дней
dd = int(input('delta days: '))
delta = datetime.timedelta(days = dd)
#Вывод нужной даты
date = d + delta
print(date.year,date.month, date.day)



