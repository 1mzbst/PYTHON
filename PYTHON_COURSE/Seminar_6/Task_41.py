# 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Массив чисел вводится в одну строку через пробел. Массив состоит из целых чисел.
# Пример:
# 5 1 3 7 9 6 -> 1
# 3 4 3 6 5 8 7 -> 3

# Решение

list_1 = [5, 1, 3, 7, 9, 6]
list_2 = [3, 4, 3, 6, 5, 8, 7]
new_list = []
count = 0

# for i in range(1,len(list_1) - 1):
#     # print(list_1[i])
#     if (list_1[i] > list_1[i - 1]) & (list_1[i] > list_1[i + 1]):
#         count += 1
# print(count)

for i in range(1,len(list_2) - 1):
    # print(list_1[i])
    if (list_2[i] > list_2[i - 1]) & (list_2[i] > list_2[i + 1]):
        count += 1
print(count)

#____________________________________________________________________________________________________________________
