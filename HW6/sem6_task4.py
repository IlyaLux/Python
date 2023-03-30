# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Список дружественных чисел:
# (220, 284)
# (1184, 1210)
# (2620, 2924)
# (5020, 5564)
# (6232, 6368)
# (10744, 10856)
# (12285, 14595)
# (17296, 18416)
# (63020, 76084)
# (66928, 66992)
# (67095, 71145)
# (69615, 87633)
# (79750, 88730)

num = int(input("Введите проверяемое число: "))
def divider_sum(a):
    result = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            result += i
    return result


for i in range(1, num):
    divider_sum(i)
    if divider_sum(divider_sum(i)) == i and i != divider_sum(i) and i < divider_sum(i):
        print(f'Пара дружественных чисел -"{i}" - "{divider_sum(i)}"')
