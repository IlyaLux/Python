# new_list = [i for i in range(10)]   # создание списка
# print(new_list)


# # 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# import random
#
# numb_list = [random.randint(0, 20) for _ in range(20)]
# print(numb_list)
# my_set = set(numb_list)
# print(my_set)
# print(len(my_set))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

import random

list_len = int(input("Введите длину списка: "))
shift = int(input("Введите на сколько элементов сдвигаем список: "))

my_list = [_ for _ in range(0, list_len)]
print(my_list)

# for i in range(shift):
#     my_list.insert(0, my_list.pop())
# print(my_list)

print(my_list[len(my_list)-shift:] + my_list[:len(my_list)-shift])
