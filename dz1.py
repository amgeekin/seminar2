"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
"""

n = int(input('Введите количество монеток '))
counter = 0
for _ in range(n):
    coin = int(input('Введите значение 1 - "орёл" или 0 - "решка": '))
    counter += coin
if counter == n or counter == 0:
    print('Все монеты лежат одной и той же стороной вверх, переворачивать не надо.')
elif counter <= n // 2:
    print('Минимальное количество монет, которые нужно перевернуть ', counter)
else:
    print('Минимальное количество монет, которые нужно перевернуть ', n - counter)
