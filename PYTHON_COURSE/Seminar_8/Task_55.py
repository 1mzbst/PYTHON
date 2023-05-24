# Test
# with open ('test.txt', 'w', encoding='utf - 8') as file:
#     file.write('Привет мир!')

# with open ('test.txt', 'a', encoding='utf - 8') as file:
#     file.write('\nПривет мир!')

with open ('test.txt', 'r', encoding='utf - 8') as file:
    data = file.readlines()

data[1] = 'Новая строка\n'


with open ('test.txt', 'w', encoding='utf - 8') as file:
    data = file.readlines(data)



with open ('test.txt', 'r', encoding='utf - 8') as file:
    print(file.read())
    







# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

