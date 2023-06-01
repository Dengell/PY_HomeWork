# Хакер Василий получил доступ к классному журналу и хочет 
# заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

n = int(input())
array = [int(i) for i in input().split()][:n]

min_value = array[0]
max_value = array[0]
for i in range(1, len(array)):
   if min_value > array[i]:
      min_value = array[i]
   elif max_value < array[i]:
      max_value = array[i]
for i in range(len(array)):
   if array[i] == max_value:
      array[i] = min_value
print(array)