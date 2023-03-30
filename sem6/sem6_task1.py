# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
import random
num_1 = int(input("Введите количество элементов в первом списке: "))
my_list_1 = [random.randint(1,20) for _ in range(num_1)]
print(my_list_1)
num_2 = int(input("Введите количество элементов в первом списке: "))
my_list_2 = [random.randint(1,20) for _ in range(num_2)]
print(my_list_2)

list_result = []

for item in my_list_1:
    if item not in my_list_2:
        list_result.append(item)

print(list_result)

my_list_3 = [item for item in my_list_1 if item not in my_list_2]
print(my_list_3)