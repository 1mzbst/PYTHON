# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


#РЕШЕНИЕ


def find_count_of_slog (source_list: str):

    """Считает количество гласных в каждом элементе переданного списка"""

    count = 0

    for i in source_list:

        if i == 'а':

            count +=1

    return count


def check_for_rithm(song: str):

    """Проверяет есть ли в строке ритм"""

    #Сортируем переданную строку на элементы

    phras_list = song.split()

    #Приминяем счетчик гласных к каждому элементу 

    list_with_song = list(map(find_count_of_slog, phras_list))

    #Проверяем на равенство каличества гласных в каждом элементе
    
    rithm = all(i == list_with_song[0] for i in list_with_song)

    if rithm:

        return print('Парам пам-пам')
    
    else:

        return print('Пам парам')
    

song = 'пара-ра-рам рам-пам-папам па-ра-па-да'

check_for_rithm(song)
