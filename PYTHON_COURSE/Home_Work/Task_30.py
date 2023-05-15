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


# an = first_number + (last_number - 1) * difference

# def arifm_progres (first_number:int, difference: int, last_number:int):
#     for i in range(first_number,last_number,difference):  # это и есть прогрессия
#         print(i)


first_number = int(input())
print(first_number)
# last_number = int(input())
# difference = int(input())
# arifm_progres(first_number,difference,last_number)