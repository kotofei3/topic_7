# numbers = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]
#
# count = 0
# print("Числа, кратные", 5, "или", 7, "и больше 100:",end=" ")
# for i in range(0, len(numbers)):
#     n = numbers[i]
#     count = int(n)
#     if (count % 5 == 0 or count % 7 == 0) and count > 100:
#         print(count, end=" ")

# _______________________________________________
numbers = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

print("Числа, кратные", 5, "или", 7, "и больше 100:", end=" ")
for num in numbers:
    num = int(num)

    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        print(num, end=" ")
