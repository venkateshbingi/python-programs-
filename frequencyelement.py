input_list = [1, 2, 2, 3, 4, 4, 4]
frequency_dict = {}
for item in input_list:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1
print(frequency_dict)
