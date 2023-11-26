num: int = int(input('Введите целое положительное число: '))

for i in range(1, num + 1):
    spase = num - i
    for j in range(spase):
        print(' ', end='')

    stars = i * 2 - 1
    for _ in range(stars):
        print('*', end='')

    print()

for i in range(num - 2, -1, -1):

    spase = num - i - 1

    for j in range(spase):
        print(' ', end='')

    star = i * 2 + 1
    for _ in range(star):
        print('*', end='')

    print()
