# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент(a1),
# разность(d) и количество элементов(n) нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

# a1 = 1
# n = 5
# d = 2

# an = a1 + (n-1) * d
# print(an)


#Решение


first_number = int(input('Enter the first number '))

range_number = int(input('Enter the range of list '))

difference = int(input('Enter the difference '))

last_number = 1

new_list = []


for i in range(range_number):

    new_list.append(first_number + (last_number - 1) * difference)

    # an = first_number + (last_number - 1) * difference

    last_number += 1


print(new_list)

#_____________________________________________________________________________________________