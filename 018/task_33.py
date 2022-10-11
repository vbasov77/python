# 34). Даны два файла, в каждом из которых находится запись многочлена, 
# приравненного к нулю. 
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые)


with open('file_1.txt', 'w', encoding='utf-8') as file:
    file.write('7')
with open('file_2.txt', 'w', encoding='utf-8') as file:
    file.write('5')

with open('file_1.txt','r') as file:
    file_1 = int(file.readline())

with open('file_2.txt','r') as file:
    file_2 = int(file.readline())

sum = file_1 + file_2
with open('sum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{sum}')