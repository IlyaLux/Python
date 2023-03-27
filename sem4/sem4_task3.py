# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
k = 10
import random

new_array = []

for i in range(k + 1):
    new_array.append(random.randint(1000, 9999))
print(f'1 этап: {new_array}')

# # 2
# num = int(input("Введите цифру, которую нужно удалить: "))
# for i in range(len(new_array)):
#     temp = new_array[i]
#     temp2 = 0
#     while temp > 0:
#         if temp % 10 == num:
#             pass
#         else:
#             temp2 = temp2 * 10 + temp % 10
#         temp = int(temp / 10)
#     new_array[i] = temp2
# print(new_array)
import string
# 2.2
num = input("Введите цифру, которую нужно удалить: ")
for index in range(len(new_array)):
    new_array[index] = str(new_array[index]).replace(num, '')
    # if str(num) in str(new_array[index]):
    #     new_array[index] = int(str(new_array[index]).replace(str(num), ''))
print(new_array)

# 3
for i in range(len(new_array)):
    while len(new_array[i]) > 1:
        new_array[i] = str(sum(list(map(int, list(new_array[i])))))
    # while new_array[i] > 9:
    #     new_array[i] = int(new_array[i] / 100) + (new_array[i] % 100 - new_array[i] % 10) // 10 + new_array[i] % 10
print(new_array)

# 4
new_array = set(new_array)
print(new_array)