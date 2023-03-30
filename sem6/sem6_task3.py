# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

import random

num = int(input("Введеите количество элементов в списке: "))
my_list = [random.randint(1, 10) for _ in range(num)]
print(my_list)

dict = {}
for i in my_list:
    dict[i] = dict.get(i, 0) + 1
print(dict)

s = 0
for key, value in dict.items():
    s += value // 2
print(f'Количество пар в списке = {s}')

# count = 0
# for item in range(0, len(my_list)+1):
#     count += my_list.count(item)//2
#     print(count)
# print(count)

