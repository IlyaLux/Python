def calk2(a, b):
    return a*b


def math(op, x, y):
    print(op(x, y))

#1
# def calk1(a, b):
#     return a+b
#2
# calk1 = lambda a,b: a + b

#3
math(lambda a,b: a + b, 5, 10)
