# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и 
# использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3

def vvod(n):
   if n == 0:
      return ''
   k = int(input())
   return vvod(n - 1) + f' {k}'


n = int(input())
print(vvod(n))
# v(2) -> ' 4' + ' 3' = ' 4 3'
#           |
#         "" + ' 4' = ' 4'
#           |
#          ""