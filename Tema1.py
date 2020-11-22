my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_ordered_list = my_list.copy()
my_ordered_list.sort()

print("Lista ordonata ascendent este : ")
print(my_ordered_list)
print("\n")

my_other_ordered_list = my_list.copy()
my_other_ordered_list.sort(reverse=True)
print("Lista ordonata descendent este : ")
print(my_other_ordered_list)
print("\n")

my_even_sliced_list = my_ordered_list[1::2]
print("Numerele pare din lista sunt : ")
print(my_even_sliced_list)
print("\n")
my_odd_sliced_list = my_ordered_list[::2]
print("Numerele impare din lista sunt : ")
print(my_odd_sliced_list)
print("\n")
my_multiple_by_3_list = my_ordered_list[2::3]
print("Multiplii de 3 din lista sunt : ")
print(my_multiple_by_3_list)
print("\n")








