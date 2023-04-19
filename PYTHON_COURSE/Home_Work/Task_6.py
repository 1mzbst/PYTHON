# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
#  где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# Решение

# from random import randint # Подсмотрел в интернетах
# number = randint(99999, 1000000)
# print(F"Your ticket is {number}.")
# firstHalf = number // 1000
# secondHalf = number % 1000
# sumFH = firstHalf // 100 + firstHalf // 10 % 10 + firstHalf % 10
# print(f'The sum of the first half of ticket is {sumFH}')
# sumSH = secondHalf // 100 + secondHalf // 10 % 10 + secondHalf % 10
# print(f'The sum of the second half of ticket is {sumSH}')
# if sumFH == sumSH:
#     print (f"The ticket {number} is lucky, huray!")
# else:
#     print(f"The ticket {number} is not lucky, sorry!")

#________________________________________________________________________________________________________
