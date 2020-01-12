# функции 1
# описание функции
# def hello(name, word):
#     print(f'Hello, {name}. Say {word}')

# hello('Alex', 'hi')
# hello('Katy', '<hello></hello>')


# def get_sum(a, b):
#     return a + b


# print(get_sum(22, 20))
# print(get_sum(11, 30))
# print(get_sum(222, 55))

# Задача: вывести таблицу умножения с 2-мя входными данными

def print_table(a, b):
    for i in range(a, b + 1):
        for j in range(1, 10):
            print(i * j, end="	")
        print('\n')


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print_table(a, b)
