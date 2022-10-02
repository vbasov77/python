n = 3

def get_numbers(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return list

list = get_numbers(n)
print (list)