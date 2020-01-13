# использование именованных аргументовы
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d


# print(get_sum(1, 2))


# def get_sum(*args):
#     print(sum(args))


# get_sum(1, 2, 3)


# def func(**kwargs):
#     return kwargs


# print(func(a=1, b=2, c=3))


def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args[1])
    print(kwargs)


f(1, 2, 3, 4, c=20, z=2000)
