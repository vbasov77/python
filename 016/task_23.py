# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7

from re import X


n = int(input('Введите число N'))
i = 2
list = []
temp = n
while i <= temp:
    if not temp % i:
        list.append(i)
        temp //= i
        i = 2
    else:
        i += 1
print(list)