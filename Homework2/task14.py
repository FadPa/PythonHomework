# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

num = int(input('Введите число: '))
degree = 1
while degree < num:
    print(degree)
    degree *=2