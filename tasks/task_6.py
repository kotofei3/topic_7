number: int = abs(int(input('Введите целое число: ')))

count: int = 0
running: bool = True
while running:
    number = number // 10
    count += 1
    if number == 0:
        running = False

print('Количество цифр в числе:', count)
