# Count the values associated with a key in a dictionary using loops
input_dict = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
count_dict = {}
for key, value in input_dict.items():
    count_dict[key] = len(value)
print(count_dict)
