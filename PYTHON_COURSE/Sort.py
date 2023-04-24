# def quick_sort(array):
#     """Быстрая сортировка"""
#     if len(array) <=1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greator = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greator)
# print(quick_sort([14,5,8,3,4,5,6,4,2,64]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k =0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len (left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len (right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,23,34,3,4,5,6,6,2]
merge_sort(list1)
print(list1)            
            