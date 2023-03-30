# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
numbers = int(input("Введите количество элементов: "))
my_list = [random.randint(1, 100) for _ in range(numbers)]

print(my_list)

find_num = int(input("Поиск ближайшего числа к числу: "))
nearest_num = my_list[0]
dist = abs(find_num - nearest_num)

for num in my_list:
    if abs(num - find_num) < dist:
        dist = abs(find_num - nearest_num)
        nearest_num = num

if my_list.count(find_num):
    print(f'число {find_num} есть в списке')
else:
    print(f'ближайшее число - {nearest_num}')
