# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

data = list(map(int,data))
print(data)