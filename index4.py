my_list = [1, 2, 3, 4, 5]
item_to_find = 4
index = -1
for i in range(len(my_list)):
    if my_list[i] == item_to_find:
        index = i
        break
print(index)
