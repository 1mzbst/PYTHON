d = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
d2 = dict.fromkeys(['D','G'],2)
d3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
d4 = dict.fromkeys([ 'F', 'H', 'V', 'W', 'Y'], 4) 
d5 = dict.fromkeys(['K'], 5)
d6 = dict.fromkeys(['J', 'X'], 8)
d7 = dict.fromkeys(['Q', 'Z'], 10)
d8 = dict.fromkeys(['!' , ',', '?', ':', ';' , '.', '...', '-', ' '], 0)
d.update(d2 | d3 | d4 | d5 | d6 | d7 | d8)
print(d)
str = 'Chamber subject then september finished limited minutes order replied avoid sister. Under meant quick pretty moment hills trees. Met within removal'
str_up = str.upper()
print(str_up)
sum = 0
for i in str_up:       
    sum += d.get(i)
print (sum)