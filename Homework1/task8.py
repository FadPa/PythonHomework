# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

a = int(input('Ведите количество долек по горизонтале: '))
b = int(input('Ведите количество долек по вертикали: '))
c = int(input('Ведите количество долек которое хотите отломить: '))

if ((c % a == 0) or (c % b == 0)) and (c < a * b):
    print('У Вас всё получилось!')
else:
    print('Нет!')