# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

#Решение

from random import randint
array = []
numN = int(input('Enter the length of array(N): '))
# print('Enter the digits of the list: ')
for i in range(numN):
    i = randint(0,9)
    # i = int(input())
    array.append(i)
print(f'It is the list that we got : {array}')
find_num = int(input('Enter the digit what you want to find: '))  # искомое значение X
find_num_for_print = find_num #значение для печати в консоль

# value_check = array[0]
# value_find = 0
# for j in array:
#     value_find = abs(j - find_num) # подсмотерел в интернетах
#     if value_find < value_check:
#         result = j
#         value_check = value_find
# print(f"The nearest number to {find_num_for_print} is {result} ")

# 

# print(f'Result is {min(array, key = lambda y: abs (y-find_num))}') # подсмотрел в записи с семинара. Крутая штука! :)




#___________________________________________________________________________________________