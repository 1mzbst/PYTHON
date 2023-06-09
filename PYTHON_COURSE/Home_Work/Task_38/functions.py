def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО ')
    phone_num = input('Введите номер телефона ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    result = [contact for contact in book if info in contact]
    return result


def search_and_rewrite() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите заменить: ')
    result = search(data, contact_to_find)
    print(f"Вот эта строка будет заменена: {''.join(result)}")
    answer = int(input("Введите 1 если Да, 2 если Нет, 3 или любую другую цифру если передумали делать замену -> "))
    if answer == 1:
        new_name = input('Введите ФИО для замены: ')
        new_telephone = input('Введите номер телефона для замены: ') 
        new_data = data.replace(''.join(result), (f'{new_name} | {new_telephone}') )
        with open('book.txt', 'w', encoding='utf-8') as file:
            file.write(new_data)
        print('Справочник изменён.')
    elif answer == 2:
        return search_and_rewrite()
    elif answer == 3:
        exit
    else: 
        show_data()
    # print(new_data)
    

                
