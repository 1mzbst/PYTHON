# def find_data() -> None:
#     """Печатает результат поиска по справочнику."""
#     with open('book.txt', 'r', encoding='utf-8') as file:
#         data = file.read()
#     contact_to_find = input('Введите, что хотите ')
#     result = search(data, contact_to_find)
#     print(result)

# with open('book.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#     data1 = data.split('\n')
#     print(type(data1))
#     for i in data1:
#         if i == 'Партной Ираклий Яковлевич | 86541237890':
#             data1[i] = "qwert qwerqwer"
#         print(i)

    # book = book.split()
    # print(book)
#     contact_to_find = input('Введите, что хотите ')
# def search(book: str, info: str) -> list[str]:
#     """Находит в списке записи по определенному критерию поиска"""
#     book = book.split('\n')
#     result = [contact for contact in book if info in contact]
#     return result

# print(search(data, contact_to_find))


# data = 'фио | номер телефона\n\
# фио1 | номер телефона1\n\
# Исаев Владислав Иванович | +814881481848\n\
# Крутой Игорь Сергеевич | +5231265489'
# print(data)
# contact_to_find = input('Enter ')

# print(search(data, contact_to_find))