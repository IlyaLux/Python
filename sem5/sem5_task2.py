# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
import math


def simple(a):
    if a in [1, 2, 3]:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True


print(simple(1234165784123))
