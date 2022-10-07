# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

count = 5
list = []
odd_numbers = []

for i in range(count):
    num = randint(1, 10)
    list.append(num)

for j in range(1, len(list), 2):
  odd_numbers.append(list[j])
odd_str = ', '.join(map(str, odd_numbers))
print(f'Изначальный список {list}')
print(f'на нечётных позициях элементы ', odd_str, 'Ответ: ', sum(odd_numbers))


