list = [1,2,2,3,3,3]

uniq_list = []
for i in list:
    if i not in uniq_list:
       uniq_list.append(i)
print(uniq_list)    