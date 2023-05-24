# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# В качестве примера характеристики можно взять проверку четности из лекции, а можно придумать свою.

list1 = [-1, -2, -3, -4, -5, -6]
print(list(map(lambda x: x < 0, list1)))
# print(list2)

# numbers = [1, 2, 3, 22, 21]
#
# print(all(map(lambda x: str(x) == str(x)[::-1], numbers)))