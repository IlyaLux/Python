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

numbers = int(input("Введите количество элементов: "))
my_list = [i for i in range(1,numbers+1)]
# my_list = [randint(1, 10) for _ in range(1, numbers + 1)]

print(my_list)

find_num = float(input("Поиск ближайшего числа к числу: "))
whole_num = int(find_num + (0.5 if find_num > 0 else -0.5))

if whole_num in my_list:
    print(whole_num)
else:
    if whole_num > max(my_list):
        print(max(my_list))
    else:
        print(min(my_list))