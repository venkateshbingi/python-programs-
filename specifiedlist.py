input_list = ['red', 'green', 'white', 'black', 'pink', 'yellow']
indices_to_remove = [0, 4, 5]
output_list = []
for i in range(len(input_list)):
    if i not in indices_to_remove:
        output_list.append(input_list[i])
print(output_list)
