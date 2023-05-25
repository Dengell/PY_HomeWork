# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

list_1 = [int(i) for i in input().split()]
step = int(input("Введите кол-во сдвигов: "))
step = step % len(list_1)
result_list = [list_1[i - step] for i in range(len(list_1))]
print(result_list)

# list_1 = [int(i) for i in input().split()]
# step = int(input("Введите кол-во сдвигов: "))
# step = step % len(list_1)
# result_list = list()
# for i in range(len(list_1)):
#     result_list.append(list_1[i - step])
# print(result_list)

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k):
#     t=list[0]
#     for i in range(len(list)-1):
#         list[i]=list[i+1]
#     list[-1]=t
# print(list)
        
# # 2 вариант 

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k-1):
#     tmp = list[-1]
#     list.insert(0, tmp)
#     list.pop()
# print(list)

# 3 вариант решения задачи

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k-1):
#     list.insert(0, list.pop()) # list.pop - извлекает последний элемент, 
# print(list)                    # list.insert(0, - ставит его на нулевую позицию