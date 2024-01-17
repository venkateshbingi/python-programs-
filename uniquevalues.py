input_list = [1, 2, 3, 3, 3, 4, 4]
unique_values = []
for i in input_list:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)