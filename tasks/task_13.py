number_user: int = int(input('Введите целое положительное число: '))
count: int = 1
for i in range(1, number_user + 1):

    for _ in range(i):
        print(count, end=' ')
        count += 1

    print()

# todo: еолизовать через цикл while
