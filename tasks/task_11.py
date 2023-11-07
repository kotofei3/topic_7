number: int = int(input('Введите целое положительное число: '))

for i in range(1, number + 1):
    for j in range(i):
        print(i, end=' ')
    print()

# __________________

i = 1
while i <= number:

    j = 0
    while j < i:
        print(i, end=' ')
        j += 1
    print()

    i += 1
