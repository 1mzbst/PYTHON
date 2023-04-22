# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#  В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, 
# X – 8 очков; Q, 
# Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12


# Эту задачу хочется осознать самому. Хоть и подсмотрел принцип решения на семинаре, 
# надо, в конечном счёте, домыслить самостоятельно. Спасибо за понимание и авансы.

d = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
d2 = dict.fromkeys(['D','G'],2)
d3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
d4 = dict.fromkeys([ 'F', 'H', 'V', 'W', 'Y'], 4) 
d5 = dict.fromkeys(['K'], 5)
d6 = dict.fromkeys(['J', 'X'], 8)
d7 = dict.fromkeys(['Q', 'Z'], 10)
d.update(d2)
d.update(d3)
d.update(d4)
d.update(d5)
d.update(d6)
d.update(d7)
# print (d)
# b = d.get('D')
# print(b)
# a = d.values()
# print(a)

# str = 'exhibition'
# str = 'Chamber subject then september finished limited minutes order replied avoid sister. Under meant quick pretty moment hills trees. Met within removal'
str = 'Chamber subject then september finished limited minutes order replied avoid sister'
str_up = str.upper()
print(str_up)
sum = 0
for i in str_up:
    sum += d.get(i)
    if i == ' ':
        i = 0
print (sum)
