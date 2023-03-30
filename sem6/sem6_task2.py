# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного
import random

num = int(input("Введеите количество элементов в списке: "))
my_list = [random.randint(1, 15) for _ in range(num)]
print(my_list)
count = 0
for i in range(1, num - 1):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        count += 1
print(count)
