# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

numbers = list(map(int, input("Введите через пробел начало списка, разницу между соседними элементами и количество "
                              "элементов: ").split()))

my_list = []
for i in range(1, numbers[2]+1):
    my_list.append(numbers[0] + (i - 1) * numbers[1])
print(my_list)
