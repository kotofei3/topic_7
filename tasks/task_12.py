# number: int = int(input('Введите целое положительное число: '))


# for i in range(1, number + 1):
#     spase = number - i
#
#     for j in range(spase):
#         print(' ', end=' ')
#
#     for _ in range(i * 2 - 1):
#         print(i, end=' ')
#
#     print()

# -------------

# todo: реализовать через цикл while
num: int = int(input('Введите целое положительное число: '))
i: int = 1
count: int = 0
while i <= num:
    count += 1

    space = num - i

    j = 1
    while j <= space:
        print(' ', end='')
        j += 1

    k = 0
    while k < i:
        print('*', end=' ')
        k += 1
    print()

    i += 1
print('iter osnov ciclsa', count)
