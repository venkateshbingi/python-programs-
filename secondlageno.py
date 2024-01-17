number_list = [1, 3, 4, 5, 0, 2]
max_num = float('-inf')
second_max_num = float('-inf')
for num in number_list:
    if num > max_num:
        second_max_num = max_num
        max_num = num
    elif num > second_max_num and num < max_num:
        second_max_num = num
print(second_max_num)