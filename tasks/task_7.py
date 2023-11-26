num: int = int(input('Введите число: '))

prime_num: int = 2

while prime_num <= num:
    if num % prime_num == 0:
        print(prime_num, end=' ')
        num //= prime_num
    else:
        prime_num += 1
