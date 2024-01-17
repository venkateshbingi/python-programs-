my_list = [10, 20, 30, 40, 50]
item_to_find = 40
index = -1
for i in range(len(my_list)):
    if my_list[i] == item_to_find:
        index = i
        break
print(index)
