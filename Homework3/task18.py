# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь 
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
print('Введите список через пробел:')
a = [int(i) for i in input().split()]
print('Введите число:')
n = int(input())  
find_num = 0

for i in range(len(a)):
    if a[i] < n:
        find_num = -find_num
    else:
        find_num = find_num + 0
    if a[i] >= n and a[i] - n <= find_num - n:
        find_num = a[i]
    elif a[i] <= n and find_num - n <= a[i] - n:
        find_num = a[i]
print(find_num)
