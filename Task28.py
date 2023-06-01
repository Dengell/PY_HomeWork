# Задача 28: Вводится десятичное число. Реализовать алгоритм его перевода
# в двоичную систему счисления через рекурсию. Нельзя использовать функцию bin()

# *Пример:*
#     10
#     *Вывод:*
#     1010

x = []
def convert(b):
    if (b == 0):
        return x
    dig = b % 2
    x.append(dig)
    convert(b // 2)
a = int(input("Введите число: "))
convert(a)
x.reverse()
print("Двоичная форма числа:")
for i in x:
    print(i, end=' ')

# print(f"{int(input()):b}")
