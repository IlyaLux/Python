# фибоначи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fib(num):
    if num in [0, 1]:
        return num
    return fib(num - 2) + fib(num - 1)


print(fib(5))
  