# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 
def power(num, deg):
    if deg == 1:
        return num
    if deg == 0:
        return 1
    if deg != 1:
        return (num * power(num, deg - 1))
num = int(input("Введите число: "))
deg = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(num, deg))