# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

A = []
n = int(input("Введите количетсво элементов в массиве: "))
for i in range(1, n+1):
    A.append(i)
print(*A)
x = int(input("Введите число x: "))
dif_min = x
for i in range(len(A)):
    if A[i] == x:
        break
    if abs(x-A[i]) < dif_min:
        dif_min = A[i]
print(f'Самый близкий по величине элемент {A[i]}')