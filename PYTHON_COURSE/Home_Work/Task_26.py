# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# Решение

def power (a,b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return 0
    else:
        return power(a ,a ** (b - 1))

result = power(3,5)
print(result)
    

