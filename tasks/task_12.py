number: int = int(input('Введите целое положительное число: '))



for i in range(1, number + 1):
    spase = number - i

    for j in range(spase):
        print(' ', end=' ')

    for _ in range(2 * i - 1):
        print('*', end=' ')

    print()

# -------------

# todo: реализовать через цикл while