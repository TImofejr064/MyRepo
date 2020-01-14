from datetime import date, datetime
import locale

# date
# today = date.today()
# print(today) # 2020-01-13
# print(today.day) # 13
# print(today.month) # 1
# print(today.year) # 2020
# print(today.weekday()) # 0

# datetime
# now = datetime.now()
#
# print(now) # 2020-01-13 22:26:51.489233

# now = datetime.now()

# print(now) # 2020-01-13 22:29:43.846698
# print(now.day) # 13
# print(now.month) # 1
# print(now.year) # 2020
# print(now.weekday()) # 0
# print(now.hour) # 22
# print(now.minute) # 31
# print(now.second) # 35

# locale.setlocale(locale.LC_ALL, 'ru_RU')
#
# now = datetime.now()
#
# print(now.strftime('%Y %B %A'))


import os
for top, dirs, files in os.walk('/root/Рабочий стол/test/'):
    for nm in files:
        print(os.path.join(top, nm))
