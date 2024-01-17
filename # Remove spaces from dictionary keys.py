# Remove spaces from dictionary keys using loops
input_dict = {"a b": 1, "c d": 2, "e f": 3}
new_dict = {}
for key, value in input_dict.items():
    new_key = key.replace(" ", "")
    new_dict[new_key] = value
print(new_dict)