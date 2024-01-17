
# Convert a list into a nested dictionary of keys using loops
input_list = [1, 2, 3, 4]
output_dict = {}
temp = output_dict
for element in input_list:
    temp[element] = {}
    temp = temp[element]
print(output_dict)