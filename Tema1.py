# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
asc_list = my_list
asc_list.sort()
print(asc_list)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
desc_list = asc_list[::-1]
print(desc_list)

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(asc_list[1:10:2])

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(asc_list[::2])

# afișarea elementelor multipli ai lui 3.
print(asc_list[2:10:3])
