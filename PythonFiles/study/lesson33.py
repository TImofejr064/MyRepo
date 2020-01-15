# f = open('text.txt', 'r', encoding="utf8")
# # text = f.read(1)
# text2 = f.read()
# f.close()
#
# print(text2)
# print(f.encoding)

# f = open('text.txt', 'a', encoding="utf8")
# for i in range(4, 11):
#     f.write(f'Новая строка номер {i}\n')
# f.close()

# f = open('text.txt', 'a', encoding="utf8")
# lines = range(1, 101)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

f = open('text.txt', 'r', encoding="utf8")
for line in f:
    print(line, end='')
f.close()
