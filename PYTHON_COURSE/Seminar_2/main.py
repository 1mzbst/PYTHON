# flag = False
# while not flag:
#     period = int(input('Period '))
#     if not (period > 100 or period < 1):
#         flag = True

# # period = int(input('Period: '))
# count= 0
# mx_count = 0
# for i in range(period):
#     temperature = int(input('Temperature '))
#     if temperature > 0:
#         count += 1
#     else:
#         if count > mx_count:
#             mx_count = count
#         count = 0
# print(f'Max ottepel {mx_count}')

# flag = False
# while not flag:
#     period = int(input('Period: '))
#     if not (period > 100 or period < 1):
#         flag = True
# count= 0
# mx_count = 0
# for i in range(period):
#     temperature = randint(-50, 50)
#     print(f'Temperature {temperature} ')
#     if temperature > 0:
#         count += 1
#     if i == period - 1 or temperature <= 0:
#         if count > mx_count:
#             mx_count = count
#         count = 0
# print(f'Max ottepel {mx_count}')

# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Решение

# factor_N = int(input('Enter the number '))
# count = 1
# count2 = 1
# while count <= factor_N:
#     count2 *= count
#     print(count2)
#     count +=1 

# ____________________________________________________________________________________________________________



# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# о вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# Решение

watermellon_count = int(input())
min = 0
max = 0
for i in range(watermellon_count):
    i = int(input())
    if i > max:
        max = i
    if i < max:
        min = i
print(min)
print(max)


# from random import randint
# watermellon_count = int(input())
# min = 30000
# max = 0
# for i in range(watermellon_count):
#     i = randint(1,30000)
#     print(i)
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(min)
# print(max)
    
  
    
   
        
        

# ____________________________________________________________________________________________________________

