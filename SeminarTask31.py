# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# Задание необходимо решать через рекурсию

def summa_numbers(a, b):
   if b == 0:
      return a
   return summa_numbers(a + 1, b - 1)


print(summa_numbers(57, 70))