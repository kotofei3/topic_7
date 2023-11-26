start: int = int(input('Введите начало диапазона: '))
end: int = int(input('Введите конец диапазона: '))

if start < 0 or end < 0 or start == end:
    print('Некорректный диапазон')
else:
    if start > end:
        start, end = end, start
    # print(start, end)  # DEBUG
    for i in range(start, end + 1):
        count: int = len(str(i))  # длина числа

        temp = i  # копия исходнгого числа
        sum_of_digits = 0  # сумма цифр числа,возведенных в кол - во цифр
        while temp > 0:
            last = temp % 10
            power = last ** count
            sum_of_digits += power
            temp //= 10

        # исходное число равно суме цифр числа
        if i == sum_of_digits:
            print(i, end=' ')

# 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
