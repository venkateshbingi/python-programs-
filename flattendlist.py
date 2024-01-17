shallow_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = []
for sublist in shallow_list:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)