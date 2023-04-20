# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Пример:

# Ввод: 5 6 -> 2 3

# Решение

print('What are the sum of the numbers, Pete?')
sum = int(input('Enter the sum of digit what Pete made wish -> '))
print('What are the product of the numbers, Pete? ')
prod = int(input('Enter the product of digit what Pete made wish -> '))
disc = sum**2 - 4*prod
# print(disc) # значение дискриминанта
if disc < 0:
    print("There are no suitable numbers, Pete!")
if disc == 0:
    f_num = sum//2
    s_num = f_num
    print(f'The hidden numbers what you made wish Pete are {f_num} and {s_num}')
else:
    f_num = int((sum + disc**0.5)//2)
    s_num = int((sum - disc**0.5)//2)
    print(f'The hidden numbers what you made wish Pete are {f_num} and {s_num}')

# ________________________________________________________________________________________