# def get_sum(a, b):
#     """
#     Возвращает сумму двух аргументов a и b.

# 	:param a: Первый операнд
# 	:param b: Второй операнд
#     """
#     return a + b


# print(get_sum(1, 2))

# a = 5  # global


# def f():
#     a = 10  # local
#     a += 1
#     print(a)


# print(a)
# f()
# print(a)

# def f():
#     global a
#     a = 10
#     return a


# print(a)
# print(f())
# print(a)

# l = [1, 2, 3, 4]


# def f2(l):
#     def s(i):
#         return i * 2
#     return [s(i) for i in l]


# print(f2(l))


"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
 Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""


# def odd_ball(arr):
#     def find_odd(arr):
#         for i in arr:
#             if i == "odd":
#                 return arr.index(i)

#     odd_index = find_odd(arr)

#     for i in arr:
#         if isinstance(i, int) and odd_index == i:
#             return True

#     return False


# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
# print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
# print(odd_ball(["even", 10, "odd", 2, "even"]))  # True


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5.
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""


# def find_sum(n):
#     return sum([i for i in range(1, n + 1) if (i % 3) == 0 or (i % 5) == 0])


# print(find_sum(5))  # return 8 (3 + 5)
# print(find_sum(10))  # return 33 (3 + 5 + 6 + 9 + 10)


"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
# ["Ryan", "Mark", "John", "Paul"]
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
"""


def get_names(names):
	s = []
    for i in names :  
		for j in names :
			if j == i:
				s.append(i)		
    return s

print(names(["Ryan", "Kieran", "Mark", "John", "David", "Paul"]))
