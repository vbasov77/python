# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from random import randint

with open('008/file.txt', 'w') as data:
    data.write('4\n')
    data.write('5\n')
    data.write('2\n')

def get_numbers(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

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

path = '008/file.txt'
n = 10 
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(numbers)
print(datalist)
print(get_mult(numbers, datalist))