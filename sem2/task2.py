# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

numFibon = int(input("введите число Фибонначи: "))
count = 2
i = 3
a = 1
while count < numFibon:
    temp = count
    count = count + a
    a = temp
    i += 1
print(count)
if count == numFibon:
    print(i)
else:
    print(-1)
