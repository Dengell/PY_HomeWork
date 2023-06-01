# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5

# Output: yes


def check_num(n):
    flag = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'no'
    return 'yes'

n = int(input('Введите число: '))
print(check_num(n))