# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

count_coins = int(input("введите кол-во монет: "))
count_tails = 0
count_emblem = 0

for i in range(1, count_coins + 1):
    coins = randint(0, 1)
    print(coins, end=' ')
    if coins == 1:
        count_tails += 1
    else:
        count_emblem += 1
print(f'\nРешкой вверх лежат {count_tails} монет.')
print(f'\nГербом вверх лежат {count_emblem} монет.')

if count_tails > count_emblem:
    print(f'\nНужно перевернуть минимум {count_emblem} монет, лежащих гербом вверх')
else:
    print(f'\nНужно перевернуть минимум {count_tails} монет, лежащих решкой вверх')
