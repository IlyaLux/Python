# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

numbers = list(map(int, input("Введите через пробел количество элементов списка, минимальный  и максимальный элемент "
                              "диапазона").split()))
my_list = [random.randint(1, 15) for _ in range(numbers[0])]
print(my_list)

for i in range(numbers[0]):
    if numbers[1] > numbers[2]:
        if numbers[2] < my_list[i] < numbers[1]:
            print(i, end=' ')
    else:
        if numbers[1] < my_list[i] < numbers[2]:
            print(i, end=' ')


