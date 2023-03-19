# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число: "))
power_count = 1
while 2 ** power_count <= N:
    print(f'2^{power_count}={2 ** power_count}')
    power_count += 1
