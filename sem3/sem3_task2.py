# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
from random import randint

my_list = [randint(0, 10) for _ in range(10)]
# 1 вар
count = 0
print(my_list)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1
print(count)

# 2 вар
new_list = [i for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)
print(len(new_list))