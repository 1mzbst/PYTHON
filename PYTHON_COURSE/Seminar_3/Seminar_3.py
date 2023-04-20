# 17'. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# [1, 2, 3, 4, 1, 2, 3]

# Решение

# nums = [1, 2, 3, 4, 1, 2, 3]
# # print(len(set(nums)))
# # количество чисел, встречающихся ровно 1 раз
# result = []
# for i in set(nums):
#     if nums.count(i) == 1:
#         result.append(i)
# print(result, len(result))

# result1 = [i for i in set(nums) if nums. count(i) == 1]
# print(result1)


# _______________________________________________________________________________________________________________________

# 19'. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
#  K – положительное число.
# [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]

# Решение

# nums = [1, 2, 3, 4, 5]
# sdvig = int(input())
# for _ in range(sdvig): # _ когда счетчик не используется
#     nums.insert(nums.pop(0), nums.pop(len(nums)-1))
# print(nums)

# nums = [1, 2, 3, 4, 5, 6, 7]
# sdvig = int(input()) % len(nums)
# for _ in range(sdvig):
#     nums.insert(0, nums.pop())
# print(nums)

# nums = nums[-sdvig::] + nums[:-sdvig:]
# print(nums)


# _______________________________________________________________________________________________________________________

# 21'. Напишите программу для печати всех уникальных значений в словаре.
# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# Решение

# slovar = {1:3, 2: 5}
# print(list(slovar.values()))
# list_of_dicts = [{"V": "S001"}, 
#                  {"V": "S002"}, 
#                  {"VI": "S001"}, 
#                  {"VI": "S005"}, 
#                  {"VII": " S005 "}, 
#                  {" V ":" S009 "}, 
#                  {" VIII ":" S007 "}] 
# uniq_el = set()
# for i in list_of_dicts:
#     for key in i:
#         element = i[key]
#         uniq_el.add(element)
# print(uniq_el)
# #     element = list(i.values())[0]
# #     print(element)
# #     uniq_el.add(element)
# # print(uniq_el)

# uniq_el1 = set(list(i.values())[0] for i in list_of_dicts)
# print(uniq_el1)





# _______________________________________________________________________________________________________________________


# 23'. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

# Решение

# nums = [1,2,3,1,2]
# count = 0
# for i in range(len(nums)):
#     if nums[i - 1] < nums[i]:
#         count += 1
# print(count)  

# result = [nums[i] for i in range(len(nums)) if nums [i - 1] < nums[i]]
# print(len(result))
# # _______________________________________________________________________________________________________________________