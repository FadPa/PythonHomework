# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монет: '))
count = 0
print('Выберете сторону манетки 1 - орёл; 0 - решка.')
for i in range(n):
    coin = int(input('Ведите сторону:'))
    if coin == 0:
        count +=1
print(f'Вам необходимо перевернуть: {count if count<n/2 else n-count}')

