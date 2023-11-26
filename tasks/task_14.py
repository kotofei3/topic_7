number: int = int(input('Введите целое положительное число: '))

# for i in range(number, 0, -1):
#     spase = number - i
#
#     for j in range(spase):
#         print(' ', end='')
#
#     stars = i * 2 - 1
#     for _ in range(stars):
#         print('*', end='')
#
#     print()
#
# for i in range(2, number +1):
#     spase = number - i
#
#     for j in range(spase):
#         print(' ', end='')
#
#     for _ in range(i * 2 - 1):
#         print('*', end='')
#
#     print()

# ____________________

i = number
while i > 0:
    spase = number - i
    j = 0
    while j < spase:
        print(' ', end='')
        j += 1
    stars = i * 2 - 1
    k = 0
    while k < stars:
        print('*', end='')
        k += 1

    i -= 1
    print()

i = 2
while i <= number:
    spase = number - i
    j = 0
    while j < spase:
        print(' ', end='')
        j += 1
    stars = i * 2 - 1
    k = 0
    while k < stars:
        print('*', end='')
        k += 1

    i += 1
    print()
