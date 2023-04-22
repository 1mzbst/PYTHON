def summ(a: int, b:int) -> int:
    """Приниает на вход два целых числа и возваращает их сумму"""
    return a + b


def merge_list(list1: list[str], list2: list[str]) -> list[str]:
    """Сливает 2 списка в 1"""
    return list1 + list2

print(summ ('1', '6'))
nums1 = ['1', '2']
nums2 = ['3', '4']
print(merge_list(nums1, nums2))
