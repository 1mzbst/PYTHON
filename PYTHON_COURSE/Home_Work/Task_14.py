# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.

# Пример:

# Ввод: 13 -> 1, 2, 4, 8

# Решение

numberN = int(input("Enter the maximum Number: "))
count = 0
result = 0
while numberN > result:
    result = 2**count
    if result < numberN:  print(result)
    count += 1 
# ____________________________________________________________________________________________
