# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Решение

# Дописать через рандом и положить в списки

from random import randint

first_n = int(input('Enter the count of first set of numbers: '))
second_n = int(input('Enter the count of second set of numbers: '))

first_set = set()
second_set = set()

# for i in range(first_n):
#     i = int(input('Number of the first set, please: '))
#     first_set.add(i)
# print(first_set)

# for i in range(second_n):
#     i = int(input('Number of the second set, please: '))
#     second_set.add(i)
# print(second_set)

for i in range(first_n):
    i = randint(1,15)
    first_set.add(i)
print(first_set)

for i in range(second_n):
    i = randint(1,15)
    second_set.add(i)
print(second_set)

union_sets = first_set.intersection(second_set)
if union_sets == set(): print('The cross set is empty')
else: print(f'The cross set is {union_sets}')






