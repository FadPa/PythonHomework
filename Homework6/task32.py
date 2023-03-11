# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = int(input('Введите количество элементов массива: '))
arr=[random.randint(-50, 50) for i in range(n)]
print(*arr)
min=int(input("min= "))
max=int(input("max= "))
arr_2=[]

if max >= min:
    for i in range(len(arr)):
        if max>=arr[i] and min<=arr[i]:
            arr_2.append(i)
    print("Количество индексов:",len(arr_2))
    print("Индексы:",arr_2)
else:
    print ('Вы ввели некорректный диапазон.')
