# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from itertools import count
from random import randint


count = 4
list = []
list2 = []

for i in range(count):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and count > len(list)/2:
        count -= 1
        result = list[i] * list[count]
        list2.append(result)
        i += 1

print(list)
print(list2)