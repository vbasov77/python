# 18). Реализуйте алгоритм перемешивания списка.
import random

list = [2, 7, 8, 6, 1]
print ("Оригинальный список: " + str(list))

for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
     
print ("Смешанный список: " +  str(list))