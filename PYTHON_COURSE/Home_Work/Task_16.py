# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

#Решение

array = []
count = 0
numN = int(input('Enter the length of array(N): '))
print('Enter the digits of the list: ')
for i in range(1,numN+1):
    i = int(input())
    array.append(i)
print(array)
find_num = int(input('Enter the digit what you want to find: '))  # искомое значение X
# for j in array:
#     if j == find_num:
#         count+=1
# print(f'The number of repeated digit is {count}')

# result = [i for i in array if i == find_num] # comprehension style
# print(f'The number of repeated digit is {len(result)}')

#______________________________________________________________________________________________________________________