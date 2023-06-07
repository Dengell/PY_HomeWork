# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Задайте количество элементов массива: '))
list = []
for i in range(n):
    list.append(random.randint(-10, 10))
print(list)

min_num = int(input('Задайте минимальный элемент диапазона: '))
max_num = int(input('Задайте максимальный элемент диапазона: '))

for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        print(i, end=' ')