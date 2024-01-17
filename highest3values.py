input_dict = {'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
values_list = list(input_dict.values())
values_list.sort(reverse=True)
highest_values = values_list[:3]
print(highest_values)
