# number: int = int(input('Введите целое положительное число: '))
#
#
# for i in range(1, number + 1):
#     spase = number - i
#
#     for j in range(spase):
#         print(' ', end=' ')
#
#     for _ in range(i * 2 - 1):
#         print('*', end=' ')
#
#     print()

# -------------
num: int = int(input('Введите целое положительное число: '))
i: int = 1

while i <= num:
    space = num - i

    j = 0
    while j < space:
        print(' ', end=' ')
        j += 1

    k = 0
    while k < i * 2 - 1:
        print('*', end=' ')
        k += 1
    print()

    i += 1
