beginning: int = int(input('Введите начало диапазона: '))
end_number: int = int(input('Введите конец диапазона: '))
if beginning > end_number:
    beginning, end_number = end_number, beginning
for i in range(beginning, end_number + 1):
    if i % 2 == 0:
        print(i)
    elif beginning == end_number:
        print(0)
