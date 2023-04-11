# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Решение:

# number = int(input())
# sum = number // 100 + number // 10 % 10 + number % 10
# print(sum)

#___________________________________________________________________________________________________

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
#     7 -> "нельзя определить"

# sum = int(input())
# Kate = 2 * sum // 3
# Pite = Kate // 4
# Serge = Pite
# if sum == Kate + Pite + Serge:
#     print (f"{sum} -> {Pite} {Kate} {Serge}")
# else:
#     print (f"{sum} -> нельзя определить")

#___________________________________________________________________________________________________

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
#  где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

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

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# print("Enter the quantity pieces of a chocolate of first side")
# width = int(input()) 
# print("Enter the quantity pieces of a chocolate of second side")
# length = int(input()) 
# print("Enter the quantity would you want to get by one try.")
# quantity= int(input()) 
# if quantity % width == 0 or quantity % length == 0:
#     print(f'You can divide the chocolate dimensions {width} x {length} on {quantity} pieces by one try.')
# else:
#     print(F'You cannot divide the chocolate on {quantity} pieces by one try.')

#________________________________________________________________________________________________________