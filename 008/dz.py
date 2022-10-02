# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

from random import randint
path = '008/file.txt'

with open(path, 'w') as data:
    data.write('4\n')
    data.write('5\n')
    data.write('2\n')

def get_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return list

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

n = 3
datalist = get_data_from_file(path)
list = get_list(n)

print(list)
print(datalist)
print(get_mult(list, datalist))