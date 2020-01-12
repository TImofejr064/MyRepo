# import os
# from random import *
# import time

# path = os.getcwd()
# print(f'Путь к данному файлу - {path}')

# while True:
#     print('Случайное чилсо от 1 до 100 - ', randint(1, 100))
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     shuffle(l)
#     print('Случайно отсортированный список - ', l)
#     time.sleep(2)

import libs as l


print(l.get_count('Ехал грека через реку', 'е'))
print(l.get_len('Ехал грека через реку'))