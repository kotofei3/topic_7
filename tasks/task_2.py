multiplication: int = int(input('Введите число:'))

print('Таблица умножения для числа', multiplication, 'с помощью цикла while:')
num: int = 1
while num <= 10:
    print(multiplication, '*', num, '=', multiplication * num)
    num += 1

multiply: int = int(input('Введите число:'))

print('Таблица умножения для числа', multiply, 'с помощью цикла for:')

increase: int = 1
for i in range(increase, 10 + 1):
    print(multiply, '*', i, '=', multiply * i)
