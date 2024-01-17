# Sort a list alphabetically in a dictionary using loops
input_dict = {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
for key in input_dict:
    input_dict[key].sort()
print(input_dict)