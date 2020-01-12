# import os
# from random import *
# import time

#
#


# while True:
#     print('Случайное чилсо от 1 до 100 - ', randint(1, 100))
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     shuffle(l)
#     print('Случайно отсортированный список - ', l)
#     time.sleep(2)

from . import libs

print(libs.get_count('Ехал грека через реку', 'е'))
print(libs.get_len('Ехал грека через реку'))


