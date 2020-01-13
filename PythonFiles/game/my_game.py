# игра угадай число  v1.0

import random

print('Привет, ты играешь в игру угадай число!')


def game():
    random.seed()
    guessed_number = random.randint(1, 100)
    print('Программа загадала случайное число от 1 до 100')
    while True:
        attempt = int(input('Введите число: '))
        if guessed_number == attempt:
            return print('Круто, ты угадал!\n')
        elif guessed_number > attempt:
            print('Загаданное число больше!\n')
        elif guessed_number < attempt:
            print('Загаданное число меньше!\n')

game()

while True:
    play_or_not = str(input('Хочешь продолжить игру? [д/н]\n'))
    if play_or_not == "д":
        game()
    else : break

print('Игра закончилась, возвращайся!')
