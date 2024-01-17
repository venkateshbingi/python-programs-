input1 = [1,2,3,4]
input2 = [1,2]
difference_list = []
for i in input1:
    if i not in input2:
        difference_list.append(i)
print(difference_list)