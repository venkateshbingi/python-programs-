list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 1]
is_circular_identical = False
if len(list1) == len(list2):
    for i in range(len(list1)):
        if all(list1[j] == list2[(i+j) % len(list2)] for j in range(len(list1))):
            is_circular_identical = True
            break
print(is_circular_identical)
