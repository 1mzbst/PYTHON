new_list = [1, 2, 3, 5, 8, 15, 23, 38]
sec_list = []


# def sqw(a, b): return a**b.


for i in new_list:
    if (i % 2) == 0:
        sec_list.append((i, i ** 2))
print(sec_list)
