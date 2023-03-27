# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

input_string = list(input("Введите строку: "))
print(input_string)

my_dict = dict()
for item in set(input_string):
    my_dict.setdefault(item, 0)
print(my_dict)

for key, value in my_dict.items():
    for i in range(len(input_string)):
        if input_string[i] == key:
            if value > 0:
                input_string[i] = f'{key}_{value}'
            value += 1

result_str = ''
for i in input_string:
    result_str += f'{i} '
print(result_str)
