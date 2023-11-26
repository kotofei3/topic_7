# n: list = []
# count: int = 0
# num: int = 0
# for i in range(1, 10 + 1):
#     soar: list = n.append(i)
#     count += 1
#     num += count
# print("iter = ", count)
# print("sum_num_iter = ", num)
#
# print("conclusion_lista:\n", sep=".", end=" ")
# for i in range(1, len(n) + 1):
#
#     module: int = int(i)
#     if module % 2 == 0:
#         print(module, "=", True)
#     else:
#         print(False, "=", module)

# even_numbered: int = 1
#
# check: bool = True
# print("Вывод: ")  # - это было не обязательно но мне так нравится,прошу прощения
# while check:
#     if even_numbered % 2 == 0:
#         print(even_numbered)
#     if even_numbered > 20:
#         check: bool = False
#     even_numbered += 1

# 2 - это рабочий код

# number: int = 1
# count: int = 0
# kol_chet: int = 0
#
# while count <= 20:
#     if number % 2 == 0:
#         kol_chet += 1
#         print(number)
#     number += 1
#     count += 1
# print("chet", kol_chet, end=' <- ')


# num: int = 1
#
# num_2: int = 20
#
# count: int = 0
#
# for i in range(num, num_2 + 1):
#     if i % 2 == 0:
#         count += 1
#         print('chet', i)
# print('chet = ', count)


# arithmetic: int = int(input(': '))
#
# count: int = 0
#
# number: int = 0
#
# method: bool = True
#
# while method:
#
#     number += 1
#     count += number
#
#     if number >= arithmetic:
#         method: bool = False
#     if number < 0:
#         print("Число должно быть больше или равно", 1)
#
# print("Сумма всех чисел от ", 1, "до", arithmetic, "равна", count)

# n: list = []
# count = 0
# while len(n) < 5:
#     user_num: int = int(input(":"))
#     letter: list = n.append(user_num)
#     count += 1
#     if count > 5:
#         False
# for i in n:
#     print(i, end=' ')
#     if i % 2 == 0:
#         print(True, "arithmetic_chet = ", i)
#     else:
#         print(False)


# print(int(n[0])+ 1)
# n = ['1']
# a = int(n[0])
# print(a)


# ---way--- 1

# number: int = int(input('Введите число:'))
#
# num: int = 1
#
# count: int = 0
#
# print('Сумма всех чисел от', num, 'до ', number, 'равна', end=' ')
#
# while num <= number:
#     count = count + num
#     num += 1
# print(count)


# n: list = [1, 2, 3]
# draw: list = []
# count: int = 0
# i: int = 0
# running = True
# while running:
#     count = draw.append(n)
#     print(draw)
#     if len(draw) >= 3:
#         running = False
#


# n: list = [1, 2, 3]
# draw: list = []
# count: int = 0
# i: int = 0
#
# while i < len(n):
#     count = draw.append(n[i])
#     i += 1
#     print(draw)


# n = []
# count = 0
# for i in range(-10, -20, -2):
#
#     count = n.append(i)
# print(n)


# cookie_shapes = ['круглая', 'квадратная', 'звездная']
# cookie_sizes = ['маленькое', 'среднее', 'большое']
#
# for shape in cookie_shapes:
#     for size in cookie_sizes:
#         print('выпекамем', size, shape)

# - разбирал пример из TOPIC - 7 ВЛОЖЕННЫЙ WHILE
# ----------------------------------------------

# cookie_shapes: list = ['круглая', 'квадратная', 'звездная']
# cookie_sizes: list = ['маленькое', 'среднее', 'большое']
#
# i_shape_index: int = 0
#
# while i_shape_index < len(cookie_shapes):
#     i_size_index = 0
#     while i_size_index < len(cookie_sizes):
#         shape = cookie_shapes[i_shape_index]
#         size = cookie_sizes[i_size_index]
#         print('Bake', size, shape, 'cookie')
#         i_size_index += 1
#     i_shape_index += 1

# ----------------------------------------------


# height: int = 5
# width: int = 3
# rows: int = 2
#
# count: int = 0
# count_2: int = 0
# count_sum:int = 0
#
# for i in range(height):
#     count += 1
#     for j in range(width):
#         count_2 += 1
#         for w in range(rows):
#             count_sum += 1
#             print(w,count_sum)
#
#         print()
#
# print('count1', count)
# print('count2', count_2)

# _________________________________________________
# letter: list = ['red', 'blue', 'green', 'black', 'yellow', 'orange']
# count: int = 0
#
# for i in range(len(letter)):
#     count += 1
#     for j in range(i + 1):
#         print(letter[i])
# print('count_sum', count)
# __________________________________________________


# letter: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# count = 0
#
# for row in letter:
#
#     for j in row:
#         count += 1
#         print('row=', j, end=' ')
#     print()
#
# print(count)


