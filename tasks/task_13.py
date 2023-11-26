# number_user: int = int(input('Введите целое положительное число: '))
# count: int = 1
# for i in range(1, number_user + 1):
#
#     for _ in range(i):
#         print(count, end=' ')
#         count += 1
#
#     print()

# -------------------

number: int = int(input('Введите целое положительное число: '))
count: int = 1

i: int = 1
while i <= number:

    j = 0
    while j < i:
        print(count, end=' ')

        j += 1
        count += 1
    print()
    i += 1
