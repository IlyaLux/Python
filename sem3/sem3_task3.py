# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной последовательности bn удалили одно число,
# а оставшиеся перемешали. Найти удаленное число.
import random
n = int(input("Введите кол-во чисел в последовательности: "))
numb_list = [i for i in range(1, n+1)]
print(numb_list)

new_list = numb_list.copy()
new_list.pop(int(input("Какой элемент удалить: ")))

random.shuffle(new_list)
print(new_list)

print(set(numb_list).difference(set(new_list)))





