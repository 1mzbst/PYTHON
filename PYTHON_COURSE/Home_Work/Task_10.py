# # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# # Определите минимальное число монеток, которые нужно перевернуть, 
# # чтобы все монетки были повернуты вверх одной и той же стороной.
# # Выведите минимальное количество монет, которые нужно перевернуть. 
# # С клавиатуры вводятся число монет и сами монеты построчно.

# # Пример:

# # Ввод: 1 1 1 1 0 0 -> 2

# # Решение

coins = int(input('Hi, enter the amount of coins, please: '))
count = 0
count2 = 0
print('Heads are 0, tails are 1.')
for i in range(coins):
    i = int(input('Please, enter the digit: '))
    if i == 0:
        count += 1
    if i == 1:
        count2 +=1
print(count, count2)        
if count > count2:
    print(f'The minimal counts to flip over of the coins are {(count - count2)}')
if count2 > count:
    print(f'The minimal counts to flip over of the coins are {(count2 - count)}')
else:
    print('The counts to flip is equally')
        
# # _______________________________________________________________________________________
