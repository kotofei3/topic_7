if (user_number := int(input('Введите число:'))) < 0:
    print('Факториал определен только для натуральных чисел.')
else:
    factorial: int = 1
    count: int = 0
    while count < user_number:
        count += 1
        factorial *= count
    print('Факториал числа', user_number, 'равен', factorial)

# factorial: int = 1
# for i in range(1, int(input('Введите число: ')) + 1):
#     factorial *= i
# print(factorial)
