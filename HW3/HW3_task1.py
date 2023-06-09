# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

numbers = int(input("Введите количество элементов: "))
# my_list = [i for i in range(1,numbers+1)]
my_list = [randint(1, 10) for _ in range(1, numbers + 1)]
print(my_list)

find_num = int(input("Введите искомое число: "))
count = 0
for i in range(len(my_list)):
    if find_num == my_list[i]:
        count += 1
print(f'Искомое число встречается {count} раз')
print(my_list.count(find_num)) # сколько раз значение встречается в списке
