# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 

# n = int(input('Введите число'))
# result = [round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)]
# print (result)
# print (round(sum(result), 3))

# Второе решение

while True:
    num = input('Введите целое положительное число:  ')
    try:
        num = int(num)
        if num > 0:
            break
        else: print('Число отрицательное')
    except ValueError:
        print('Число должно быть положительным')
list = []
for i in range(1, num + 1):
    elem = round(((1 + 1/i)**i), 2)
    list.append(elem)
print(list)
print(f'Сумма последовательности равна: {sum(list)}')