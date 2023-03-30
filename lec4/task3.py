my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for item in my_list:
#     if item % 2 == 0:
#         res.append((item, item**2))
# print(res)


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


res = select(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print (res)