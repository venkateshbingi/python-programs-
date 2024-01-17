main_list = [2, 4, 3, 5, 7]
sub_list = [4, 3]
is_sublist = False
for i in range(len(main_list) - len(sub_list) + 1):
    if main_list[i:i + len(sub_list)] == sub_list:
        is_sublist = True
        break
print(is_sublist)
