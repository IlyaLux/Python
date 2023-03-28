# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree_num(x, y):
    return x if y == 1 else x * degree_num(x, y - 1)
    # if b == 1:
    #     return a
    # else:
    #     return a * degree_num(a, b-1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
res = degree_num(A, B)
print(res)
