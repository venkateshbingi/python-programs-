# Combine values in a Python list of dictionaries using loops
input_list = [{1: 10}, {2: 20}, {3: 30}]
result_dict = {}
for d in input_list:
    for key, value in d.items():
        result_dict[key] = value
print(result_dict)