my_list = [1, 2, 3, 4]
smallest_num = float('inf')
second_smallest_num = float('inf')
for num in my_list:
    if num < smallest_num:
        second_smallest_num = smallest_num
        smallest_num = num
    elif num < second_smallest_num and num != smallest_num:
        second_smallest_num = num
print(second_smallest_num)
