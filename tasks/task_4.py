if (number := int(input('Введите число: '))) <= 0:
    print('Число должно быть больше или равно', 1)
elif number == 1:
    print(number)
else:
    num: int = 1
    count_sum: int = 0

    while num <= number:
        count_sum += num
        num += 1
    print('Сумма всех чисел от', 1, 'до', number, 'равна', count_sum)
