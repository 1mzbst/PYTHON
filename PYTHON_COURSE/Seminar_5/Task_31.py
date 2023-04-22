# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи|


# def fib(n):
#  if n < 1:
#     return 1
#  return fib(n - 1) + fib(n - 2)

# list_1 = [0]
# for i in range(1, 10):
#     list_1.append(fib(i - 2))
# print(list_1)
# #Вариант 2

fib1 = 1
fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print("Значение этого элемента:", fib2)