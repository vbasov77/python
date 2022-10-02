# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 

n = int(input('Введите число'))
result = [round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)]
print (result)
print (round(sum(result), 3))
